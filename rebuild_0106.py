"""
rebuild_0106.py
Reconstrói var _D no index.html a partir de Produtos DDMM.xlsx + Sinonimos DDMM.xlsx.
normStr alinhada com JavaScript: remove acentos, hifens→espaço, PONTOS→espaço.

Regras de inclusão e bloqueio:
  - SITUA='A' (Ativo): item pode voltar ao estoque → incluir no banco
  - SITUA='I' (Inativo): item descontinuado → EXCLUIR do banco
  - Bloqueado (blk:1): sem estoque, não calcula preço, pede avaliação do farmacêutico
      · Se coluna INDBLOQUEIO existir: INDBLOQUEIO in ('S','O') → blk:1
      · Se não existir: PRVEN=0 (sem preço = sem estoque) → blk:1
  - EQUIV numérico NÃO é sinônimo — é fator de conversão, ignorado na lista de s[]
  - Sinônimos lixo filtrados: XXXXX*, SEM USO, CAMPO SEM USO
"""
import json, base64, re, unicodedata, warnings
import pandas as pd

warnings.filterwarnings('ignore')

HTML_PATH = r'C:\Agente Alpha\index.html'
PROD_PATH = r'C:\Agente Alpha\produtos 2206 (1).xlsx'
SIN_PATH  = r'C:\Agente Alpha\Sinonimos 2206.xlsx'

# ── normStr alinhada com JS (inclui dots→space) ─────────────────
def normStr(s):
    if not s: return ''
    s = str(s).lower().strip()
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('-', ' ')
    s = s.replace('.', ' ')   # ← alinha com JS: dots viram espaço
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# ── Padrão de sinônimos lixo a ignorar ──────────────────────────
_LIXO_RE = re.compile(r'^x{3,}|^sem uso$|^campo sem uso', re.IGNORECASE)

def is_lixo(nome):
    """Retorna True se o nome é lixo (XXXXX, SEM USO, etc.)"""
    n = str(nome).strip()
    return bool(_LIXO_RE.match(n)) or n.upper().startswith('XXXXX')

# ── Conversões de campo ──────────────────────────────────────────
def conv_preco(v):
    """PRVEN: 0→0; <10 = R$/g direto; >=1000 = R$/kg (÷1000)"""
    try: v = float(v)
    except: return 0.0
    if v == 0 or pd.isna(v): return 0.0
    if v >= 1000: return round(v / 1000, 6)
    return round(v, 6)

def conv_dens(v):
    """DENSIDADE: 0→None; >=10 = valor/1000; <10 = direto"""
    try: v = float(v)
    except: return None
    if v == 0 or pd.isna(v): return None
    if v >= 10: return round(v / 1000, 4)
    return round(v, 4)

def conv_teor(v):
    """TEOR: 0→None; valor/100000 → decimal 0-1"""
    try: v = float(v)
    except: return None
    if v == 0 or pd.isna(v): return None
    return round(v / 100000, 6)

def conv_fator(v):
    """FATOR: 0→1.0; valor/1000"""
    try: v = float(v)
    except: return 1.0
    if v == 0 or pd.isna(v): return 1.0
    if v >= 100: return round(v / 1000, 4)
    return round(v, 4)

# ── 1. Ler Excel ─────────────────────────────────────────────────
print(f"Lendo {PROD_PATH}...")
df_prod_raw = pd.read_excel(PROD_PATH, header=0)
print(f"  {len(df_prod_raw)} produtos (total)")
print(f"  Ativos (A): {len(df_prod_raw[df_prod_raw['SITUA']=='A'])} | Inativos (I): {len(df_prod_raw[df_prod_raw['SITUA']=='I'])}")
# Apenas SITUA='A' — inativos são descontinuados, excluir do banco
df_prod = df_prod_raw[df_prod_raw['SITUA']=='A'].copy()
print(f"  Usando apenas ativos: {len(df_prod)} itens")
tem_indbloqueio = 'INDBLOQUEIO' in df_prod.columns
print(f"  Coluna INDBLOQUEIO: {'SIM' if tem_indbloqueio else 'NAO — usando PRVEN=0 como bloqueado'}")

print(f"Lendo {SIN_PATH}...")
df_sin = pd.read_excel(SIN_PATH, header=0)
print(f"  {len(df_sin)} registros de sinônimos")

# ── 2. Construir mapa de sinônimos {cdpro → [(nome, key), ...]} ──
print("\nConstruindo mapa de sinônimos (sem EQUIV numérico, sem lixo)...")
sin_map = {}   # {cdpro: [(nome_sin, key_sin), ...]}
filtrados_lixo = 0
filtrados_equiv = 0

for _, row in df_sin.iterrows():
    try:
        cid = int(row['CDPRO'])
    except:
        continue

    sname = str(row['DESCRPRD']).strip() if pd.notna(row['DESCRPRD']) else ''
    if not sname or sname.upper() == 'NAN':
        continue

    # Filtrar lixo (XXXXX, SEM USO, CAMPO SEM USO)
    if is_lixo(sname):
        filtrados_lixo += 1
        continue

    if cid not in sin_map:
        sin_map[cid] = []

    sk = normStr(sname)
    if sk and sk not in [x[1] for x in sin_map[cid]]:
        sin_map[cid].append((sname, sk))

    # NOTA: EQUIV é fator de conversão numérico — NÃO adicionar como sinônimo
    # (Bug presente na versão anterior que adicionava "0.0", "1000.0" etc.)

sin_total = sum(len(v) for v in sin_map.values())
print(f"  {len(sin_map)} produtos com sinônimos")
print(f"  {sin_total} sinônimos válidos")
print(f"  {filtrados_lixo} entradas lixo filtradas (XXXXX / SEM USO)")

# ── 3. Construir INS array ────────────────────────────────────────
print("\nConstruindo INS array...")
ins_list = []
skipped = 0

for _, row in df_prod.iterrows():
    nome = str(row['DESCRPRD']).strip() if pd.notna(row['DESCRPRD']) else ''
    if not nome or nome.upper() == 'NAN':
        skipped += 1
        continue

    try:
        cid = int(row['CDPRO'])
    except:
        cid = 0

    pe = conv_preco(row['PRVEN'])
    d  = conv_dens(row['DENSIDADE'])
    t  = conv_teor(row['TEOR'])
    f  = conv_fator(row['FATOR'])

    k = normStr(nome)

    # Sinônimos
    syns    = sin_map.get(cid, [])
    s_names = [x[0] for x in syns]
    sk_keys = [x[1] for x in syns]

    # Bloqueado = sem estoque, não calcula preço, pede avaliação do farmacêutico
    # · Se INDBLOQUEIO existir: usar 'S' ou 'O'
    # · Se não existir: PRVEN=0 indica sem estoque → bloqueado
    if tem_indbloqueio:
        bloqueado = str(row.get('INDBLOQUEIO', 'N')).strip().upper() in ('S', 'O')
    else:
        bloqueado = (pe == 0.0)

    ins = {'n': nome, 'k': k}
    ins['pe'] = pe
    ins['p']  = pe

    if bloqueado:
        ins['blk'] = 1  # sem estoque — não calcula preço

    if f != 1.0:
        ins['f'] = f
    if t is not None and t < 1.0:
        ins['t'] = t
    if d is not None:
        ins['d'] = d
    if s_names:
        ins['s']  = s_names
        ins['sk'] = sk_keys

    ins_list.append(ins)

print(f"  {len(ins_list)} itens incluídos, {skipped} ignorados (nome vazio)")

# ── 4. Verificações ───────────────────────────────────────────────
print("\nVerificações:")
with_price = sum(1 for x in ins_list if (x.get('pe') or 0) > 0)
print(f"  Com preço > 0: {with_price}/{len(ins_list)}")
with_dens  = sum(1 for x in ins_list if x.get('d'))
print(f"  Com densidade: {with_dens}")
with_syns  = sum(1 for x in ins_list if x.get('s'))
print(f"  Com sinônimos: {with_syns}")
total_sin_final = sum(len(x.get('s', [])) for x in ins_list)
print(f"  Total entradas sinônimos: {total_sin_final}")

# Verificar que "0.0" NÃO aparece como sinônimo
falsos = [x for x in ins_list if '0.0' in x.get('s', [])]
print(f"  Itens com '0.0' como sinônimo (deve ser 0): {len(falsos)}")

# Amostras de produtos-chave
print("\nAmostras de busca:")
samples = [
    'DUTASTERIDA', 'MINOXIDIL', 'FINASTERIDA',
    'VITAMINA D3', 'COLECALCIFEROL', 'L RHAMNOSUS',
    'BIOTINA', 'ACIDO HIALURONICO', 'DAPAGLIFLOZINA',
    'TESTOSTERONA', 'PROGESTERONA', 'ESTRADIOL'
]
for s in samples:
    k = normStr(s)
    match = next((x for x in ins_list if x['k'] == k or (x.get('sk') and k in x['sk'])), None)
    if not match:
        match = next((x for x in ins_list if k in x['k']), None)
    if match:
        syns_preview = (match.get('s') or [])[:3]
        print(f"  {s!r}: {match['n']} pe={match.get('pe',0):.4f} sins={syns_preview}")
    else:
        print(f"  {s!r}: NAO ENCONTRADO")

# ── 5. Serializar e substituir var _D ────────────────────────────
print("\nCodificando base64...")
js_json = json.dumps(ins_list, ensure_ascii=False, separators=(',', ':'))
new_b64 = base64.b64encode(js_json.encode('utf-8')).decode('ascii')
print(f"  JSON: {len(js_json):,} chars | Base64: {len(new_b64):,} chars")

print("Atualizando index.html...")
with open(HTML_PATH, encoding='utf-8') as f:
    html = f.read()

# Localizar var _D
m = re.search(r"var _D\s*=\s*'([^']+)'", html)
if not m:
    m = re.search(r'var _D\s*=\s*"([^"]+)"', html)
if not m:
    print("ERRO: var _D nao encontrado!")
    exit(1)

old_ins = json.loads(base64.b64decode(m.group(1)))
print(f"  DB anterior: {len(old_ins)} itens")

old_str = m.group(0)
new_str = f"var _D = '{new_b64}'"
html_new = html.replace(old_str, new_str, 1)

if html_new == html:
    print("ERRO: substituicao sem efeito!")
    exit(1)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html_new)

print(f"  index.html atualizado! ({len(html_new):,} chars)")

# Verificação final
m2 = re.search(r"var _D\s*=\s*'([^']+)'", html_new)
ins2 = json.loads(base64.b64decode(m2.group(1)))
print(f"  DB novo: {len(ins2)} itens ok")

print("\nConcluido!")
