# Use uma imagem oficial do Rust como base
FROM rust:latest

# Instala o mdBook usando Cargo
RUN cargo install mdbook

# Define o diretório de trabalho no container
WORKDIR /work

# Expõe a porta usada pelo mdBook serve
EXPOSE 3000

# Comando padrão: inicia o servidor mdBook
CMD ["mdbook", "serve", "-n", "0.0.0.0"]
