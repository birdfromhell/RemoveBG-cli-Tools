import requests
from rich import print
from rich.prompt import Prompt


def prompt_user() -> dict:
    api = str("BW5D7u8MGCqfcKtxCMBnUopc") if Prompt.ask("Masukan Api anda (https://www.remove.bg/api) 0 Untuk API Default? ") == "0" else ""
    file_name = Prompt.ask("Masukan Nama File (Tanpa extension file : jpg ,png)")
    method = Prompt.ask("Masukan File Lewat 1.Link - 2.Folder ", choices=["1", "2"], default="1")
    bgcolor = Prompt.ask("Masukan Warna Background (Ex:red,green / hex:81d4fa ? Enter --> Tidak")
    source = Prompt.ask("Masukan Link") if method == "1" else Prompt.ask("Masukan path File")

    return {
        'api': api,
        'file_name': file_name,
        'method': method,
        'bgcolor': bgcolor,
        'source': source
    }


def send_request(data: dict):
    response = ''
    headers = {'X-Api_Key': data['api']}

    if data['method'] == '1':
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            data={
                'image_url': data['source'],
                'size': 'auto',
                'bg_color': data['bgcolor']
            },
            headers=headers
        )
    else:
        with open(data['source'], 'rb') as image_file:
            response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                files={'image_file': image_file},
                data={'size': 'auto'},
                headers=headers,
            )

    return response


def write_file(response, file_name):
    if response.status_code == requests.codes.ok:
        with open(f'{file_name}.png', 'wb') as out:
            out.write(response.content)


def check_status_code(response):
    match response.status_code:
        case 403:
            print("[bold red]Api Key Salah[/]")
        case 429:
            print("[bold red]Rate limit exceeded[/]")
        case 200:
            print("[bold green]Finish[/]")


def main():
    user_inputs = prompt_user()
    response = send_request(user_inputs)
    check_status_code(response)
    if response.status_code == requests.codes.ok:
        write_file(response, user_inputs['file_name'])


if __name__ == "__main__":
    main()