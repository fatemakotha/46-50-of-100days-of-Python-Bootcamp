import smtplib
import os

my_email = os.environ.get("EMAIL")
my_app_pass = os.environ.get("PASSWORD")

with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
    connection.ehlo()
    connection.login(user=my_email, password=my_app_pass)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="fatema.alam.kotha@gmail.com",
        msg=f"hi"
    )