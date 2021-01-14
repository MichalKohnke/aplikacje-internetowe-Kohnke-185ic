# aplikacje-internetowe-Kohnke-185ic
# Autor: Michał Kohnke

						Sprawozdanie nr.8

						Lab8 - plik  
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab8/lab8_screeny/signup.png)

						Lab8- login
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab8/lab8_screeny/login.png)

						Lab8- user_list
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab8/lab8_screeny/user_list.png)

						Lab8- worker 1
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab8/lab8_screeny/worker1.png)

						Lab8- worker 2
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab8/lab8_screeny/worker2.png)

Komentarz: 
- plik consumers.py - połączenie między klientem a serwerem, każdy połączony użytkownik będzie dodany do grupy 'users' i odbierał wiadomości od serwera. Wyświetlanie użytkowników oraz ich status połączenia(przygotowany model w models.py).
- plik routing.py - podobne działanie do konfiguracji Django URL; korzystamy z channel_routing i route() zamiast urlpatterns i url(); linkowane są funkcje klienta do WebSocket.
- plik a_base.html oraz jego rozszerzenie user_list.html - przygotowanie wiadomości obsługujących połączenie klienta z serwerem używająć WebSocket.
- pliki sign_up.html oraz log_in.html - logowanie klienta(do tego odpowiednie urls'y oraz views'y).

						Sprawozdanie nr.7

						Lab7 - Celery
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab7_celery/lab7_screeny/home.png)

						Sprawozdanie nr.6

						Lab6 - stworzona podstrona home, użytkownik niezalogowany 
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab4/lab6_screeny/home_unlog.png)

						Lab6 - stworzona podstrona home, użytkownik zalogowany 
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab4/lab6_screeny/home_log.png)

						Sprawozdanie nr.4

						Lab4 - API V1 
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab4_screeny/lab4_screeny/api_v1.png)

						Lab4 - SWAGGER 
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab4_screeny/lab4_screeny/swagger.png)

						Lab4 - serializery i zezwolenia
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab4_screeny/lab4_screeny/serializers_and_permissions.png)


						Sprawozdanie nr.3

						Lab3 - strona główna 
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab2_screeny/index.png)

						Lab3 - logowanie 
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab3_screeny/login.png)

						Lab3 - logowanie przez Google
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab3_screeny/login_google.png)

						Lab3 - zalogowany przez Google
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab3_screeny/google_after_login.png)

						Lab3 - logowanie przez Facebooka
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab3_screeny/login_facebook.png)

						Lab3 - logowanie przez Facebooka(w trakcie logowania)
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab3_screeny/facebook_in_action.png)

						Lab3 - zalogowany przez Facebooka
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab3_screeny/facebook_after_login.png)

						Lab3 - ustawienia aplikacji w Google API
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab3_screeny/google_settings.png)

						Lab3 - ustawienia aplikacji w Facebook Developers
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab3_screeny/facebook_settings.png)

						Lab3 - ustawienia w adminie
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab3_screeny/admin_settings.png)




						Sprawozdanie nr.2
# Link do strony z lab2 - https://kohnkelab2.herokuapp.com/
						Lab2 - strona główna 
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab2_screeny/index.png)

						Lab2 - logowanie 
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab2_screeny/login.png)

						Lab2 - zalogowany
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab2_screeny/logged.png)

						Lab2 - rejestracja
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab2_screeny/register.png)

						Lab2 - reset hasła
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab2_screeny/password_reset.png)

						Lab2 - zmiana hasła
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab2_screeny/password_change.png)

						Lab2 - przykładowy log z wysłanym mailem o reset hasła
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/lab2_screeny/sent_emails.png)

						Sprawozdanie nr.1

						Lab1 - index.html
![alt text](https://github.com/MichalKohnke/aplikacje-internetowe-Kohnke-185ic/blob/master/Lab1_screeny/index.png)



