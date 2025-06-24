
import requests

def atualizar_like_overlay(username, likes):
    url = "https://SEU_REPLIT_LINK.replit.app/like"  # Troque para o link do seu Replit
    data = {
        "username": username,
        "likes": likes
    }
    try:
        response = requests.post(url, json=data)
        print(f"Enviado: {username} - {likes} likes. Status: {response.status_code}")
    except Exception as e:
        print(f"Erro ao enviar like: {e}")
