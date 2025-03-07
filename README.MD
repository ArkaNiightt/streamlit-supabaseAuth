# Streamlit + Supabase Auth

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.42.0-red)](https://streamlit.io/)
[![Supabase](https://img.shields.io/badge/Supabase-2.13.0-green)](https://supabase.io/)

Um template simples para implementação de autenticação em aplicações Streamlit usando Supabase como backend de autenticação.

## 📋 Visão Geral

Este projeto oferece um ponto de partida para desenvolvedores que precisam implementar autenticação em seus aplicativos Streamlit. Ele contém uma interface de login pronta, conexão com Supabase Auth e estrutura organizada para fácil expansão.

## 🔧 Funcionalidades

- ✅ Tela de login responsiva
- ✅ Autenticação via Supabase
- ✅ Proteção de rotas baseada em sessão
- ✅ Estrutura de projeto organizada
- ✅ Interface amigável com feedback visual

## 🛠️ Instalação

1. **Clone o repositório**

    ```bash
    git clone https://github.com/ArkaNiightt/streamlit-supabaseAuth.git
    cd streamlit-supabaseAuth
    ```

2. **Instale as dependências**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure as credenciais do Supabase**
    Copie o arquivo `.streamlit/secrets.exemple.toml` para `.streamlit/secrets.toml` e adicione suas credenciais:

    ```toml
    [supabase]
    SUPABASE_URL="sua_url_do_supabase"
    SUPABASE_KEY="sua_chave_anon_do_supabase"
    ```

4. **Execute o aplicativo**

    ```bash
    streamlit run src/app.py
    ```

## 📁 Estrutura do Projeto

```md
streamlit-supabaseAuth/
├── .streamlit/
│   ├── secrets.exemple.toml    # Exemplo de arquivo de configuração
│   └── secrets.toml            # (Gitignore) Suas credenciais
├── src/
│   ├── assets/                 # Imagens e recursos estáticos
│   ├── database/
│   │   ├── supabaseConection.py # Inicialização do cliente Supabase
│   │   └── supabaseQuerys.py    # Funções de consulta ao Supabase
│   ├── utils/
│   │   └── config.py           # Configurações gerais
│   ├── app.py                  # Ponto de entrada da aplicação
│   └── view.py                 # Componentes de visualização
└── requirements.txt            # Dependências do projeto
```

## ⚙️ Configuração do Supabase

1. Crie uma conta no [Supabase](https://supabase.io/)
2. Configure autenticação por email/senha no seu projeto
3. Obtenha a URL do projeto e a chave anônima
4. Adicione esses valores ao arquivo `.streamlit/secrets.toml`

## 🚀 Como Usar

1. Inicie o aplicativo
2. Faça login com as credenciais cadastradas no Supabase
3. Após autenticação, você será direcionado para a área protegida

## 🛠️ Personalização

- Modifique `view.py` para personalizar a área pós-login
- Customize a interface de login em `app.py`
- Adicione mais funcionalidades de autenticação em `supabaseQuerys.py`

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir issues ou enviar pull requests para melhorar este template.
