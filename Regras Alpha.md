# Regras Alpha — Farmácia de Manipulação
**Versão do Agente:** v4.68 | **Atualizado em:** 2026-06-12

> Este arquivo é a fonte única de regras de negócio do Agente Alpha.
> Edite aqui quando uma regra mudar e envie para o Claude atualizar o sistema.

---

## 1. CÁPSULAS

### 1.1 Tipo por Insumo — Entérica

| Insumo |
|--------|
| Alfa Amilase |
| Amilase |
| Biointestil |
| Duloxetina Cloridrato |
| Lipase |
| Pancreatina |
| Sulfasalazina |

### 1.2 Tipo por Insumo — Vegetal

| Insumo |
|--------|
| Acetil L-Carnitina |
| Ácido Lipoico |
| Biosil |
| Chronic |
| Clock |
| EVA 360 / Shatavarinas |
| Keranat |
| L Carnitina Base |
| Lipowheat |
| Modutin |
| Nutricolin |
| Oli Ola |
| Ormona |
| Reverse |
| TCM para Cápsula pó |
| TKW-10 |

> **Observações:**
> - Se a receita especificar "cápsula vegetal" ou "cápsula entérica", seguir sempre a prescrição, independentemente da lista acima.
> - **Keranat** deve ser cotada **separadamente** em cápsula vegetal, mesmo quando prescrita junto com outros insumos.
> - na receita Cápsulas Vegetais sem Corante = a Cápsula Vegetal Incolor


### 1.3 Tipo por Insumo — Oleosa (Vegetal)

- Detectada automaticamente quando um insumo do setor 200 (líquido) é prescrito em Cápsula.

### 1.4 Tamanho e Seleção

- Cápsula **n°4 Vegetal NÃO EXISTE** na farmácia → usar n°3 (upgrade silencioso, sem aviso)
- Quando a receita tiver **múltiplas fórmulas em Cápsula**, identificar o tipo (Vegetal/Entérica/Gelatinosa) **individualmente por fórmula** — não aplicar o tipo de uma fórmula para as demais.
- Se o volume da dose exceder a cápsula n°00 (951 mm³) → usar **2 cápsulas por dose**
- O volume real leva em conta a **densidade** do insumo (`ins.d`):
  - Volume (mm³) = Dose (mg) ÷ Densidade (g/cm³)
  - Exemplo: Biointestil d=0,55 → 600 mg ÷ 0,55 = 1.091 mm³ → 2 cápsulas

### 1.5 Tamanhos Disponíveis (CGEL)

| Tamanho | Volume interno |
|---------|---------------|
| n°4 | 210 mm³ |
| n°3 | 300 mm³ |
| n°2 | 371 mm³ |
| n°1 | 481 mm³ |
| n°0 | 681 mm³ |
| n°00 | 951 mm³ |

### 1.6 Preços das Cápsulas (por unidade)

| Tipo | Preço |
|------|-------|
| Gelatinosa n°4 a n°0 | R$ 0,0195 |
| Gelatinosa n°00 | R$ 0,0300 |
| Vegetal n°4 a n°0 | R$ 0,0500 |
| Vegetal n°00 | R$ 0,0600 |
| Entérica n°4 a n°0 | R$ 0,1200 |
| Entérica n°00 | R$ 0,1250 |

### 1.7 Potes para Cápsulas

| Volume | Caps n°3 | Caps n°2 | Caps n°1 | Caps n°0 | Caps n°00 | Preço |
|--------|----------|----------|----------|----------|-----------|-------|
| 60ml | 90 | 50 | 30 | 30 | 30 | R$2,00 |
| 80ml | 120 | 90 | 60 | 45 | 30 | R$2,00 |
| 110ml | 180 | 120 | 120 | 60 | 60 | R$2,00 |
| 150ml | 270 | 180 | 150 | 90 | 80 | R$2,00 |
| 230ml | 480 | 270 | 240 | 180 | 120 | R$2,00 |
| 320ml | 480 | 390 | 300 | 240 | 180 | R$2,00 |
| 500ml | 720 | 510 | 480 | 360 | 270 | R$2,50 |

### 1.8 Cálculo em Bilhões — Lactobacillos (BLH)

- Verificar sempre a concentração cadastrada do insumo em BLH/g (bilhões de UFC por grama).
- Quando a prescrição indicar X BLH / Bilhões / Bilhões de UFC, fazer a relação com o cadastro.
- Referência: BLH 100 = 100.000.000.000 unidades/g.

---

## 2. EXCIPIENTES PARA CÁPSULAS

| Situação | Excipiente | Preço/g |
|----------|-----------|---------|
| Lactobacillus / Bifidobacterium | Celulosix Lacto | R$ 0,200 |
| Liberação modificada / Ação prolongada | Celulosix Lib. Modificada | R$ 0,189 |
| Insumos com umidade (Carnitina, Ácido Lipoico, Biointestil, Colina, D-Ribose, etc.) | Excipiente para Umidade | R$ 0,060 |
| Demais casos | Excipiente Geral | R$ 0,066 |

---

## 3. SACHÊS

### 3.1 Base por Tipo

| Situação | Base | Preço/g | Qtd por sachê |
|----------|------|---------|---------------|
| Geral | Shake Nutrição | R$ 0,097 | 4g |
| Aminoácidos (Arginina, Carnitina, Alanina) | Shake Sub. Amargas | R$ 0,046 | 4g |
| PEPTISTRONG / Glutamina / Psillium / Polidextrose / Inulina | **Sem shake** | — | — |

> **Regra sem shake (itens especiais):**
> Fórmulas com **PEPTISTRONG** (item 23011), **Glutamina**, **PSILLIUM** (item 2151), **POLIDEXTROSE** (item 8804) ou **INULINA** (item 7798) **não levam base Shake**.
> Adicionar apenas 0,5g de **Aroma para Cotação - Pó** (item 24332).
> **Exceção:** se esses insumos estiverem associados com Arginina, Carnitina ou Alanina → manter a regra do Shake Sub. Amargas.

### 3.2 Aroma

- Sempre adicionar **0,5g de Aroma cotação pó** (item 24332) por sachê.
- Aplica-se a todos os sachês, inclusive os sem shake.

### 3.3 Celulose

- **NÃO adicionar Celulose** como excipiente em sachês.
- Exceção: fórmulas com Lactobacillus em **Cápsula** → usar Celulosix Lacto.

### 3.4 Tamanhos de Sachê

| Tamanho | Capacidade | Preço |
|---------|-----------|-------|
| 7×7 P | até 4g | R$ 0,1166 |
| 7×9 M | até 9g | R$ 0,1314 |
| 7×17 G | até 20g | R$ 0,1150 |

---

## 4. HORMÔNIOS

### 4.1 Detecção de Forma

- Usar forma **Hormônio** sempre que houver Estradiol, Testosterona, Estriol ou Progesterona em forma tópica (creme, gel, loção).

### 4.2 Embalagens Airless

| Volume | Preço |
|--------|-------|
| 30g | — |
| 60g | R$ 9,50 |
| 120g | R$ 18,00 |

---

## 5. MINOXIDIL

### 5.1 Cápsulas

- Sempre usar o item **21408 — Minoxidil 1/10 Cápsula** (somente para forma CÁPSULA).
- Usar preços padronizados, nas dosagens abaixo — **não usar cálculo padrão**. Se a dose prescrita for diferente das padronizadas, cobrar normalmente.
- Manter os valores desta tabela independentemente da quantidade solicitada pelo cliente.

| Dose | 30 Pix | 30 Cartão | 60 Pix | 60 Cartão | 90 Pix | 90 Cartão | 120 Pix | 120 Cartão | 180 Pix | 180 Cartão |
|------|--------|-----------|--------|-----------|--------|-----------|---------|------------|---------|------------|
| 0,5mg | R$87  | R$92  | R$115 | R$121 | R$125 | R$132 | R$140 | R$147 | R$175 | R$184 |
| 1,0mg | R$90  | R$95  | R$120 | R$127 | R$130 | R$137 | R$147 | R$155 | R$183 | R$193 |
| 1,5mg | R$105 | R$110 | R$139 | R$146 | R$172 | R$181 | R$208 | R$219 | R$275 | R$289 |
| 2,0mg | R$113 | R$119 | R$149 | R$157 | R$185 | R$195 | R$209 | R$220 | R$305 | R$321 |
| 2,5mg | R$113 | R$119 | R$163 | R$172 | R$209 | R$220 | R$219 | R$229 | R$315 | R$329 |
| 3,0mg | R$137 | R$145 | R$169 | R$179 | R$222 | R$233 | R$271 | R$286 | R$349 | R$369 |
| 3,5mg | R$145 | R$152 | R$185 | R$195 | R$239 | R$252 | R$289 | R$305 | R$369 | R$389 |
| 4,0mg | R$146 | R$154 | R$196 | R$206 | R$269 | R$292 | R$341 | R$359 | R$379 | R$399 |
| 5,0mg | R$156 | R$165 | R$206 | R$217 | R$289 | R$305 | R$351 | R$369 | R$389 | R$410 |

### 5.2 Tópico

- **NUNCA usar o item 21408** (Minoxidil 1/10 Cápsula) para uso Tópico (Externo, Capilar, Sobrancelhas).
- Quando não especificado qual Minoxidil (sulfato ou base), usar sempre o **item 54768 — Minoxidil Sulfato EU**.
- **Com** fatores de crescimento (AFGF, BFGF, IGF, VEGF, Copper Peptide):
  - Veículo: **Loção Capilar** (item 10360) + **TRICHOSOL** (item 16257)
- **Sem** fatores de crescimento:
  - Veículo: **Sol. Hidroalcóolica** (item 3306)
- MKP: sempre usar tabela **Loção Hidratante**
- Embalagem: frasco de vidro, por volume

---

## 5A. ITENS ESPECIAIS

### 5A.1 Vitamina K2

- Quando prescrito **K2** (sem especificação), usar o **item 24602 — K2** (sinônimo do item 11971 — Vitamina K2, R$2,70/g).
- **Não confundir com K2 Vital Delta** (item 23189, R$75,00/g — uso diferente, concentração reduzida).

### 5A.2 Treonato de Magnésio

- Item 15927 (Treonato de Magnésio): regra de dose por cápsula/sachê:
  - Dose **≤ 160 mg**: usar o **item 22275 — Treonato Magnésio até 160mg**
  - Dose **> 160 mg**: usar o item **15927 — Treonato de Magnésio**
- A mesma regra se aplica quando a receita especifica **Magnésio Treonato** (item 22276).

---

## 6. FÓRMULAS ESPECIAIS

### 6.1 Solução de ATA (Ácido Tricloroacético)

- Calcular **Ácido Tricloroacético** (item 50337) na concentração prescrita (X%).
- Veículo: **Água Purificada qsp** (item 20334). **Nunca usar Loção Base ou outro veículo.**
- Embalagem: frasco de vidro.
- Exemplo: "Solução de ATA 30% / Água Purificada qsp 5ml"

### 6.2 Peeling de Jessner

- **Não adicionar base** ao cálculo — cobrar apenas o volume do produto ativo (ex: Sol. Jessner).
- Para escolha de embalagem e MKP: usar tabela **Xarope**.

### 6.3 Escalonamento — Dose por Grama

- Quando a receita informa a dose em relação a **1g de base** (ex: *"Vitamina C 200mg em 1g de Creme Base, total 30g"*), multiplicar a dose pelo total de gramas:
  - Dose total = 200 mg × 30 = **6.000 mg**
- Aplica-se a: Creme, Gel, Loção, Creme Gel, Base.
- **Exceção:** se a dose já estiver em **%**, é concentração direta — não multiplicar.

### 6.4 Veículos com "qsp" no Nome

- "qsp" (= *quantidade suficiente para*) **não faz parte do nome** do veículo.
- Exemplo: *"Creme Vaginal qsp 30g"* → veículo = **Creme Vaginal**, quantidade = 30g.
- Não confundir "qsp" como parte do nome do ativo ou da base.

---

## 7. PREÇOS E MARKUP

### 7.1 Regra de Preço

- Usar sempre **preço de Venda** (`pe`) como prioritário.
- Fallback: preço de Custo (`p`) se `pe` não existir.
- **Nunca usar preço de Custo no orçamento final.**

### 7.2 Custo Fixo e Preço Mínimo

- Custo Fixo (CF): **R$ 37,50**
- Preço Mínimo (PM): **R$ 62,00**
- Fórmula: `PV = arredondar(Custo × MKP + CF)` — se PV < PM, usar PM.

### 7.3 Tabelas de MKP

- O MKP é escolhido pelo ponto da tabela **mais próximo** ao custo calculado.
- Tabelas disponíveis: **Cápsulas, Sachê, Creme/Gel, Loção Hidratante, Hormônio, Sublingual, Xarope**.

---

## 8. EMBALAGENS

### 8.1 Cremes

- **Creme Facial** (olhos, periocular, contorno, rosto, face): usar tabela específica facial.
- **Creme para área dos olhos**: usar sempre o item **11827 — Creme p/ Área Olhos**.
- **Creme Corporal**: usar tabela corporal padrão.

### 8.2 Loções

- Frasco adequado ao volume prescrito.

### 8.3 Frascos de Vidro

- Usado para: **Minoxidil Tópico** e **Solução de ATA**.
- Seleção por volume (ml).

---

## 9. REGRAS GERAIS

### 9.0 Produtos Associados — Extensivo a Sinônimos

- Todas as regras da tabela de **Produtos Associados** (PROD_ASSOC) são extensivas aos **sinônimos** do insumo principal.
- Exemplo: se o ativo é "L-Cisteína" (item 51779) e está prescrito por um sinônimo ("Cisteína HCL", "Cloridrato de L-Cisteína"), o produto associado ainda deve ser aplicado.

### 9.1 Cálculo de Custo por Forma

- **Forma tópica** (Creme, Gel, Loção, Hormônio): custo = `g × preço` (sem multiplicar por quantidade)
- **Cápsulas / Sachês**: custo = `g × quantidade × preço`

### 9.2 Conversão Automática

- **Líquidos** não entram em cápsulas/sachês (bloqueado automaticamente).
- **Sachê com qtd ≤ 2**: ajustar para 30 sachês (instrução de uso detectada como quantidade).
- **Total de ativos > 10g em cápsula**: converter automaticamente para sachê.

### 9.3 Correção Manual

- Permitir alterar manualmente o item, quando a leitura da receita for identificada como incorreta.

### 9.4 Regras por Prescritor

- **Dra. Gabriela Gomes Pedro (CRM 92265):**
  Adicionar **0,5% do item 25677 — Ess Padrão** em todas as fórmulas de:
  Creme, Loção, Gel, Omega Gold, Base Hydra Fresh, Serum e Sabonete líquido.

---

## 10. NUMERAÇÃO DE ORÇAMENTOS

- Formato: `ORC-XX-NNNN` (ex: ORC-K7-0042)
- `XX` = ID do dispositivo (2 letras, definido no primeiro uso)
- `NNNN` = sequencial por dispositivo
- Mesma receita com múltiplas fórmulas → mesmo número de ORC

---

## 11. CONTROLE DE ACESSO

- Chave atual: `ALPHA2026`
- URL de acesso: `https://lcg2026.github.io/farmacia-alpha/?k=ALPHA2026`
- Para rotacionar: alterar `ACCESS_KEY` no `index.html` + push + regerar todos os `.bat`

---

## HISTÓRICO DE ALTERAÇÕES

| Data | Versão | Alteração |
|------|--------|-----------|
| 2026-06-10 | v4.67 | Rebuild banco v2: CDSIN com EQUIV≥10 como entradas independentes (123 itens novos — Treonato Magnésio R,282/g, Magnésio Citrato, Malato, etc.); EQUIV treonato corrigido |
| 2026-06-10 | v4.66 | Ajustes100626: PROD_ASSOC extensivo a sinônimos; aviso n°4 vegetal removido; vegetal individual por fórmula (prompt); Minoxidil tópico→item 54768; K2→item 24602; Treonato ≤160mg→item 22275; rebuild banco Produtos/Sinônimos 1006 |
| 2026-06-10 | v4.65 | Fix calcSimQtd: cápsula vegetal/entérica e pote corretos na simulação de quantidade |
| 2026-06-04 | v4.64 | Sachê sem shake para Peptistrong/Glutamina/Psillium/Polidextrose/Inulina |
| 2026-06-04 | v4.63 | Prompt IA: escalonamento dose/grama; qsp no nome do veículo; Ess Padrão + Serum/Omega |
| 2026-06-02 | v4.62 | Levotiroxina doses não-padrão sempre manipulado; separador MEMED (*); PDF fix |
| 2026-06-01 | v4.61 | PDF: detecção por extensão + anthropic-beta header; max_tokens 8000 |
| 2026-06-01 | v4.60 | ATA: veículo Água Purificada + frasco vidro; regra no prompt IA |
| 2026-06-01 | v4.59 | Minoxidil 1,5mg em MINOX_PRECO e _doseKeys |
| 2026-06-01 | v4.58 | Rebuild banco Produtos/Sinônimos 0106; corrige bug EQUIV numérico (2518 sinônimos falsos) |
| 2026-05-31 | v4.57 | Reverter Extended Thinking (regressão); manter system prompt + max_tokens 6000 |
| 2026-05-31 | v4.56 | Fix _doseKeys Minoxidil cap: 0,5 e 1,0 ausentes |
| 2026-05-31 | v4.55 | System prompt separado + regras multi-fórmula + Minoxidil doses |
| 2026-05-27 | v4.46 | Botão ✏️ corrigir ingrediente no resultado; aviso BLH sem cadastro |
| 2026-05-27 | v4.45 | Remov. Celulosix sachê Lacto; ATA sinônimo; creme olhos 11827; Ess Padrão CRM 92265 |
| 2026-05-25 | v4.44 | Minoxidil 0,5mg e 1,0mg; Airless 60g R$9,50; EVA 360 vegetal |
| 2026-05-24 | v4.43 | Controle de acesso por chave URL |
| 2026-05-24 | v4.42 | Cálculo de volume real por densidade (ins.d) |
| 2026-05-24 | v4.41 | Tabela insumos × tipo de cápsula (planilha) |
| 2026-05-21 | v4.40 | Fix detecção cápsula vegetal |
| 2026-05-21 | v4.39 | Cápsula n°4 Vegetal → usar n°3 |
| 2026-05-21 | v4.38 | 6 correções Ajuste16 |
| 2026-05-19 | v4.37 | Fix bug lista vendedoras |

---

## 10. SUBLINGUAL / OROTAB / OUTROS

### 10.1 Tipos de Comprimido Sublingual

| Tipo | Forma (AI) | Capacidade |
|------|-----------|------------|
| Sublingual padrão | Sublingual | 200 mg (0,2g) |
| Orotab Diet | Orotab | 760 mg (0,76g) |

### 10.2 Insumos Obrigatórios por Comprimido

| Insumo | Item | Qtd/comp | Preço/g |
|--------|------|----------|---------|
| Aroma para cotação - pó | 24332 | 50 mg | R$ 0,1982 |
| Orotab Diet (excipiente qsp) | — | volume restante | R$ 0,21 |

- Para sublingual padrão (200mg): excipiente geral (R$ 0,066/g) qsp do volume restante
- Fórmula: qsp por comprimido = capacidade − ativo(mg) − aroma(50mg)

### 10.3 Embalagem

| Item | Capacidade | Preço |
|------|-----------|-------|
| EMB CAIXA PAPELÃO P/ OROTAB FAC (22532) | 30 unidades | R$ 0,92/cx |

- Qtd caixas = Math.ceil(n_comprimidos / 30)

### 10.4 Fórmula de Cálculo

1. Custo ativo = dose(g) × n_comp × preço/g
2. Custo aroma = 0,050g × n_comp × R/usr/bin/bash,1982/g
3. Custo excipiente = qsp(g) × n_comp × preço_excipiente/g
4. Custo embalagem = Math.ceil(n_comp/30) × R/usr/bin/bash,92
5. MKP = Tabela Progressiva (aba Sublingual — compartilhada com Outros)
6. PV = Custo × MKP + R7,50 | Mínimo R2

### 10.5 Outros (Pó em Gramas)

- Produtos vendidos em gramas: Carbonato de Cálcio, Colágeno Hidrolisado, Verisol, Psyllium em gramas, etc.
- Forma AI: **Outros**
- Sem aroma, excipiente ou embalagem padrão (embalagem informal conforme prescritor/produto)
- MKP: Tabela Progressiva Sublingual (mesma tabela)
