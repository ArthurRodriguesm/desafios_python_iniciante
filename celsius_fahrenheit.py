thermometric_scale = int(input("[1] - Celsius \n[2] - Fahrenheit \n\nEscolha a escala termonétrica para qual deseja converter: "))

temperature = float(input("Digite a temperatura: "))

conversion = 0

if thermometric_scale == 1:
    conversion = (temperature * 9/5) + 32
    print(f"{temperature}℃  -> {conversion}℉")
else:
    conversion = (temperature - 32) * 5/9
    print(f"{temperature}℉  -> {conversion}℃")