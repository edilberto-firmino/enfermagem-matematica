# 🌐 Mapa de Calor Interativo - Fortaleza

## 📍 Foco da Pesquisa

**Bairro:** Prefeito José Walter  
**Instituição:** Escola Estadual Onelio Porto  
**Objetivo:** Análise de proximidade de locais de segurança e saúde

## 📊 Dados do Mapa

- **Total de Locais:** 45 pontos de interesse
- **Postos de Saúde:** 14
- **Delegacias/Postos de Segurança:** 11
- **CAPS:** 8
- **Corpos de Bombeiros:** 9
- **Instituições Especiais:** 3 (incluindo Escola Onelio Porto)

---

## 🌐 Como Executar o Mapa de Calor como Página Web

## Opção 1: Executar com Servidor Python (Recomendado)

### Passo 1: Abra o Terminal
```bash
cd /Users/macbook/projects/enf-matematica
```

### Passo 2: Execute o servidor web
```bash
python3 servidor_web.py
```

Você verá uma mensagem como:
```
============================================================
🌐 SERVIDOR WEB DO MAPA DE CALOR - FORTALEZA
============================================================
✅ Servidor iniciando na porta 8000...
📍 Acesse: http://localhost:8000/mapa_calor_fortaleza.html
🌍 Ou para rede local: http://SEU_IP_LOCAL:8000/mapa_calor_fortaleza.html
⏹️  Pressione Ctrl+C para parar o servidor
============================================================
```

### Passo 3: Acesse a página
- **Localmente**: Abra [http://localhost:8000](http://localhost:8000)
- **Interface melhorada**: Abra [http://localhost:8000/index.html](http://localhost:8000/index.html)

---

## Opção 2: Abrir os arquivos diretamente

Se preferir não usar servidor, abra em seu navegador:
- `mapa_calor_fortaleza.html` (mapa interativo)
- `index.html` (interface com legenda e informações)

---

## 📊 Para Compartilhar com Outros

### Compartilhamento Local (Mesma Rede WiFi)

1. Execute `python3 servidor_web.py`
2. Encontre seu IP local:
   ```bash
   ipconfig getifaddr en0
   ```
   (em Windows, use: `ipconfig`)

3. Compartilhe o link: `http://SEU_IP:8000/index.html`

### Compartilhamento Online

Para compartilhar online, você pode:
- Fazer upload para GitHub Pages
- Usar serviços como Netlify ou Vercel (grátis)
- Fazer upload em um servidor web

---

## 🎨 Personalizar o Mapa

Abra o notebook `mapa_calor_fortaleza.ipynb` e:

1. Modifique as coordenadas com dados reais
2. Mude as cores dos marcadores
3. Adicione mais locais
4. Execute as células para regenerar o arquivo HTML

---

## ⚠️ Solução de Problemas

### "Port already in use"
Mude a porta no arquivo `servidor_web.py` (linha com `PORT = 8000`)

### Página não carrega
- Verifique se está na pasta correta
- Certifique-se que `mapa_calor_fortaleza.html` existe
- Limpe o cache do navegador (Ctrl+Shift+Delete)

### Para parar o servidor
Pressione `Ctrl+C` no terminal

---

## 📝 Arquivos Principais

```
enf-matematica/
├── mapa_calor_fortaleza.ipynb      (Notebook - edite aqui para personalizar)
├── mapa_calor_fortaleza.html       (Mapa interativo)
├── index.html                      (Página com interface melhorada)
├── servidor_web.py                 (Script para rodar servidor)
└── README.md                        (Este arquivo)
```

---

**✨ Pronto! Agora seu mapa está funcionando como uma página web pública!**
# enfermagem-matematica
