# Criar Data Frame
preco_gasolina = pd.read_csv('gasolina.csv', sep=',')

# Gerar o grafico
with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=preco_gasolina, x="dia", y="venda")
  grafico.set(title='Preço médio de venda da gasolina na cidade de São Paulo', xlabel='Dia', ylabel='Venda');

  fig = grafico.get_figure()
  fig.savefig(fname="gasolina.png", bbox_inches="tight")