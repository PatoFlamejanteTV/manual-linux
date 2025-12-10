# ferramenta simples que praticamente procura no site links d epágina sem links de outras páginas, etc.
# usado na indexação do Google, Bing, etc.
#
# mais informações aqui: https://www.npmjs.com/package/sitemap-generator-cli
#
# se você quiser INSTALAR ele globalmente (eu acho), use "npm install -g sitemap-generator-cli"
cd site
npx sitemap-generator-cli https://quack.is-a-good.dev/manual-linux --last-mod --change-freq daily --priority "1.0,0.95 0.90,0.85,0.80," --verbose
cd ..
#                         [link do site]                           [incluir lastmod]                                                  [incluir mais
#                                                                              [frequencia de mudanças]                                 detalhes]
#                                                                                                [prioridade da
#                                                                                                  indexação]
