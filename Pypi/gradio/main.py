import gradio as gr

def somar(num1, num2):
    return num1 + num2

demo = gr.Interface(
    fn=somar,
    inputs=[
        gr.Number(label="Primeiro Número"), 
        gr.Number(label="Segundo Número")
    ],
    outputs=gr.Number(label="Resultado"),
    title="Calculadora de Soma"
)

demo.launch()