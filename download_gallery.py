import os
import urllib.request
import ssl

# Ignorar errores de certificado SSL si ocurren
ssl._create_default_https_context = ssl._create_unverified_context

# Configuración
OUTPUT_DIR = "assets/img/gallery"

# Datos de la galería (Nombre Organización -> ID Google Drive)
gallery_data = [
    {'org': 'Asociación de Mujeres Wiwa Abu Dzibu', 'url': 'https://lh3.googleusercontent.com/d/1nJOIHbkNSG8KZpHTr_JQr6Q51Aa4l3qj=w1000'},
    {'org': 'ORVIEN (Víctimas Río Iró)', 'url': 'https://lh3.googleusercontent.com/d/1U71LIxqIK8Co29IfYW_tHtkSGXQwgqAk=w1000'},
    {'org': 'FUNDACION MICELIO', 'url': 'https://lh3.googleusercontent.com/d/1SZokjnFQKKmp8-AGGMbeoqPPd3bGijt_=w1000'},
    {'org': 'COMPAÑÍA AMÉRICA DANZA', 'url': 'https://lh3.googleusercontent.com/d/1lopAGfInMNmYdi1ObehgxgHBCFkAHguT=w1000'},
    {'org': 'FUNDACIÓN PATERPAUTT', 'url': 'https://lh3.googleusercontent.com/d/1FsVwoP10g6Nembh_VwXPvroP7DE1-hD-=w1000'},
    {'org': 'Asociación de Vecinos Granjas de San Pablo ASOVEG', 'url': 'https://lh3.googleusercontent.com/d/1CLR7uXXL5aLcb_C1_BwRnPSJFRtuoix_=w1000'},
    {'org': 'Corporación Errante Lab', 'url': 'https://lh3.googleusercontent.com/d/1aECWwrwfM89vgWUz6VnCtZZKkf7V0mRo=w1000'},
    {'org': 'Asociación de mujeres triunfadoras tejiendo vida', 'url': 'https://lh3.googleusercontent.com/d/1n5A-Fb5ZuYjhu2m5ZhVmrLv8ZdgJrM1A=w1000'},
    {'org': 'Fundación el hogar de tota', 'url': 'https://lh3.googleusercontent.com/d/1GxmfaHsHBGNo9uZnBKHeAQRVgZ9yTiTM=w1000'},
    {'org': 'asociacion de mujeres casa del sembrador', 'url': 'https://lh3.googleusercontent.com/d/1tvOgTNdFf1FAkPH7PxjoHNRcJCVbcaCy=w1000'},
    {'org': 'FUNDACION CULTURAL KYNZA XIE', 'url': 'https://lh3.googleusercontent.com/d/1MXhYItzfHWNz9Gzh8Fhtc8cb2aKXHNL2=w1000'},
    {'org': 'Corporación violeta en movimiento', 'url': 'https://lh3.googleusercontent.com/d/12uHqrQXl0_LIqIT5GheHqGki4DaBF6Pi=w1000'},
    {'org': 'Corporación para el desarrollo coral de Buga, Corpacoros', 'url': 'https://lh3.googleusercontent.com/d/1DirjE69ng7SZhNMiaL-bR91PDXIIwpku=w1000'},
    {'org': 'Corporación SIN FRONTERAS', 'url': 'https://lh3.googleusercontent.com/d/1tjlbt2axkgt2tzjCClZwpA5MXtHOaW2r=w1000'},
    {'org': 'Tierra Pazifica/BOICOP', 'url': 'https://lh3.googleusercontent.com/d/1QKq4G6hK4BydfkdH7p937Yf50YfMtNjc=w1000'},
    {'org': 'COPORACION DE DANZA DINASTIA NEGRA', 'url': 'https://lh3.googleusercontent.com/d/1-_yDGUlbkEgNATnut7tFJc_p_hpvmJ_I=w1000'},
    {'org': 'CORPORACION ULRIKA', 'url': 'https://lh3.googleusercontent.com/d/1rRhJY47X4VdTe6XnI6CGmZtY8tRdSgkM=w1000'},
    {'org': 'FUNDACION UNIDOS POR EL DESARROLLO COMUNITARIO', 'url': 'https://lh3.googleusercontent.com/d/1lvghP7OWU5w_K_snegmBOTXGHmi2ylVM=w1000'},
    {'org': 'afroresilientes', 'url': 'https://lh3.googleusercontent.com/d/1bYMsIlkGJAoOy2yOUoX3OepqeLGEbdjx=w1000'},
    {'org': 'Coral Santa María', 'url': 'https://lh3.googleusercontent.com/d/1IvqjbFidyVy48ZdVwkajeNAz2Kxhs3QK=w1000'},
    {'org': 'Fundación Socio Cultural La Nana', 'url': 'https://lh3.googleusercontent.com/d/1vFk_MOqERa-XZUd1Tlftjaj7W2Wf_YK5=w1000'},
    {'org': 'FUNDACIÓN UN MAR DE VOCES', 'url': 'https://lh3.googleusercontent.com/d/1RzQd38isbSKGrj4ACw8TIqNGSBMN2Zml=w1000'},
    {'org': 'ASOCIACION DE CAVILDOS INDIGENAS IPIALES', 'url': 'https://lh3.googleusercontent.com/d/1ssTIFHjSW0Z6LklQDfyUemoDiMhXwHjE=w1000'},
    {'org': 'Corporación CorArte', 'url': 'https://lh3.googleusercontent.com/d/1QzEO7sqsP_tu0tC-EeNdvJOtiBDQwJyP=w1000'},
    {'org': 'Fundación movimiento Hip Hop Ipiales', 'url': 'https://lh3.googleusercontent.com/d/1_CHlkd-Sezkjca7PViXOYsnfDn6H5TU9=w1000'},
    {'org': 'FUNDACIÓN CULTURAL NEWSPAPER', 'url': 'https://lh3.googleusercontent.com/d/1oP5VVfgwCMyoRwjBWDCDe1G2mjkkN0nc=w1000'},
    {'org': 'Corporación Cultural CK - Casa Kolacho', 'url': 'https://lh3.googleusercontent.com/d/16eBugG1_U1DUIUc3zDazsT-oV0Bzp8ok=w1000'},
    {'org': 'Fundación escuela de arte el círculo Hip Hop', 'url': 'https://lh3.googleusercontent.com/d/1G6-xbLkrR4Ns7_YQ_aSDhIm4srOuaaLO=w1000'},
    {'org': 'Fundación Cultura, Paz y Territorio', 'url': 'https://lh3.googleusercontent.com/d/1W-vWj2hjLw6VHjRxTrv17-xLXVdtAFTh=w1000'},
    {'org': 'Fundación Surprise City', 'url': 'https://lh3.googleusercontent.com/d/1lKVpUl_Z00kbT0YujevluNOKW2s9GKEp=w1000'},
    {'org': 'Corporación Casabeat', 'url': 'https://lh3.googleusercontent.com/d/1lmZxU_yM8tVTCJy9NaeodvHQjhy9WXYK=w1000'},
    {'org': 'Fundación 5ta con 5ta crew', 'url': 'https://lh3.googleusercontent.com/d/1TGJfhsZawzYwOEaIIobeKUMKSQ1dJqMw=w1000'},
    {'org': 'RapJudesco', 'url': 'https://lh3.googleusercontent.com/d/1mX-Q73ODWi89QUKKi_l-C9rZq5JCuKUL=w1000'},
    {'org': 'JAC AGUA BONITA 2', 'url': 'https://lh3.googleusercontent.com/d/1E8F5dae7ygM1cNaxCTnX0kHBZ5S0TMpp=w1000'},
    {'org': 'Asociación Hip Hop por Nuestra Tierra', 'url': 'https://lh3.googleusercontent.com/d/1bEOsMvHMJa7Dwd84q-crXHFAZc1Vc6FF=w1000'},
    {'org': 'Colectivo Hip Hop por la Vida', 'url': 'https://lh3.googleusercontent.com/d/1FPIkHTd4cYQ_nfvTDwNgerLCkRWK4VDK=w1000'},
    {'org': 'FUNDACIÓN BUENAVENTURA HIP HOP', 'url': 'https://lh3.googleusercontent.com/d/17SymbWLVsUrymaPYM79bD1IapGpYZfbL=w1000'},
    {'org': 'La Casa del bardo', 'url': 'https://lh3.googleusercontent.com/d/19dy6D4TVXfJa0oKW1je2o0Q8JQ7zE6cU=w1000'},
    {'org': 'Montaña Récords Catatumbo', 'url': 'https://lh3.googleusercontent.com/d/10EtrBZFUpoNui9w0xjZt0yn4yLi75B5a=w1000'},
    {'org': 'Fundación Hip Hop Peña', 'url': 'https://lh3.googleusercontent.com/d/15Mgm0b2zkyQIMl4UNmpeKuHYsC_iCz_l=w1000'},
    {'org': 'Corporacion La Tigra', 'url': 'https://lh3.googleusercontent.com/d/1dkoetMX0XJgP_6V0U6XwXMkZJrDOX0B9=w1000'},
    {'org': 'CORPORACIÓN INFLUENCERS ÉTNICOS', 'url': 'https://lh3.googleusercontent.com/d/1_HEdHTcaFC8iH62bttZqD44uHNMEkIbi=w1000'},
    {'org': 'Parchemos por Yacopí', 'url': 'https://lh3.googleusercontent.com/d/1_mjFj8EYhCC0DKm5E7hQKuFpO7F1ZdIg=w1000'},
    {'org': 'Corporación Arreglando el País', 'url': 'https://lh3.googleusercontent.com/d/1ABwDLnVGdsRE9GBVHDzdE07xK0Gz4cUQ=w1000'},
    {'org': 'Fundacion Pacifica Cultural', 'url': 'https://lh3.googleusercontent.com/d/1FL4-j11qweOQBvmn4ZaAOpbmkxzCDujw=w1000'},
    {'org': 'La Minga Muralista Kamentsa', 'url': 'https://lh3.googleusercontent.com/d/1n10eBIq5OIgKuj9SY2l_ejlPkDc96hQH=w1000'},
    {'org': 'Corporación rey de la selva', 'url': 'https://lh3.googleusercontent.com/d/1etUFCzAlhVgnc26OvLWA1pcqknrI5c-W=w1000'},
    {'org': 'CORPORACIÓN CÓDIGO ESTILO CREW', 'url': 'https://lh3.googleusercontent.com/d/1P4abW3IlMjbD4FZSjxMGiowmwuVzQT7h=w1000'},
    {'org': 'Comunicación Visual Sin Fronteras', 'url': 'https://lh3.googleusercontent.com/d/14G3zXHfqtok0OYp-AhM15HMEHG24r-ME=w1000'},
    {'org': 'The Giants Community', 'url': 'https://lh3.googleusercontent.com/d/1hpqhN0qQhig2GFdlHqcQzHoGjLI4mnQV=w1000'},
    {'org': 'Org. Desarrollo Ecosistemas Culturales', 'url': 'https://lh3.googleusercontent.com/d/1YH62fS8ZpKCzM26Z_54BliVC5g5sdEQe=w1000'},
    {'org': 'corpohuellas', 'url': 'https://lh3.googleusercontent.com/d/16QlsJc0jymlxsd1l2FWfZfNBLqmmT5on=w1000'},
    {'org': 'Corporación Calina Cumbay', 'url': 'https://lh3.googleusercontent.com/d/13PZeRmhjr2Nihzf9JjtY-Opl0zS-E8zq=w1000'},
    {'org': 'Corporación Yukuta', 'url': 'https://lh3.googleusercontent.com/d/1npd4GYgidtc8VAU6dIZq9Kuc7nhzB5y_=w1000'},
    {'org': 'NUEVO ESTILO DANCE', 'url': 'https://lh3.googleusercontent.com/d/1ZYDRM5bW3heynZwzvCO2GXvS9oU4F6_O=w1000'},
    {'org': 'Corporación Emergiendo', 'url': 'https://lh3.googleusercontent.com/d/1qrEOSL-wstvJ2seUKUA0Iwa-ryCiKue1=w1000'},
    {'org': 'FUNDACION MANGLARIA DIVERSA', 'url': 'https://lh3.googleusercontent.com/d/1POVww1zYg5Tx7I8zitXzNWoQmqjH2pBu=w1000'},
    {'org': 'Jóvenes creadores del chocó', 'url': 'https://lh3.googleusercontent.com/d/1-EKnM02WR4jZWQS9KBg2WkImXevWcZ65=w1000'},
    {'org': 'Corporación Fahrenheit 451', 'url': 'https://lh3.googleusercontent.com/d/1Y_SFloZHhNwEiUI8djzcRcW-OFMDvude=w1000'},
    {'org': 'Fundacion Amahía', 'url': 'https://lh3.googleusercontent.com/d/1ZO_Cjcd5il2jb_BUky19wUAx48iFwMS0=w1000'},
    {'org': 'Medance - Ritmo Extremo REX', 'url': 'https://lh3.googleusercontent.com/d/1Pwf5Fl3YoEVhOBY1PrM3WTqqaWEobMz_=w1000'},
    {'org': 'Fundación Linderos de Paz', 'url': 'https://lh3.googleusercontent.com/d/1z8iuyDh1duXL_TQQC1aAz7CpgtYombot=w1000'},
    {'org': 'MUSIQULTURA', 'url': 'https://lh3.googleusercontent.com/d/1XqazVqA2cfeTgtNtzo69zwcUuxvLwuq-=w1000'},
    {'org': 'RED PENSAMIENTO LATINOAMERICANO', 'url': 'https://lh3.googleusercontent.com/d/1LD1aYnCX7lwM9pscWw_psdnqqyqbEY_P=w1000'},
    {'org': 'Corporaciòn Vida-Paz', 'url': 'https://lh3.googleusercontent.com/d/13d6CnOk5X3hUhzwOQw9xILaR648POoWF=w1000'},
    {'org': 'KOMBILESA MÍ', 'url': 'https://lh3.googleusercontent.com/d/17IU9a5m01ug6KIy2pbb9izm4nAatbtMV=w1000'},
    {'org': 'Guaque - Territorialidades S.A.S', 'url': 'https://lh3.googleusercontent.com/d/1duiHZ9eXXQYKdGzjhtGKDhR9YQK7m4N_=w1000'},
    {'org': 'Corporación Elements', 'url': 'https://lh3.googleusercontent.com/d/1MeIBopLKBXM6k3U_A5Rl48_QM6DapUYL=w1000'}
]

def clean_filename(name):
    return "".join([c if c.isalnum() else "_" for c in name]) + ".jpg"

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Carpeta creada: {OUTPUT_DIR}")

    print(f"Iniciando descarga de {len(gallery_data)} imágenes...")
    
    for item in gallery_data:
        filename = clean_filename(item['org'])
        filepath = os.path.join(OUTPUT_DIR, filename)
        url = item['url']

        print(f"Descargando: {item['org']} -> {filename}")
        try:
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        except Exception as e:
            print(f"ERROR descargando {item['org']}: {e}")

    print("\n¡Proceso completado! Las imágenes están en assets/img/gallery/")

if __name__ == "__main__":
    main()
