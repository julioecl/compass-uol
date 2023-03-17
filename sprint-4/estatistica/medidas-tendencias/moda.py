from bokeh.sampledata.iris import flowers as dados

moda = dados['sepal_length'].mode()

print(moda)