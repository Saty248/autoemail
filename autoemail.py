import smtplib
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('mondal.sayantan1234@gmail.com','khdilvquacoyxlvz')
    subject='meeting link'
    body='link'

    msg=f'Subject:{subject}\n\n{body}'

    smtp.sendmail('mondal.sayantan1234@gmail.com',['mondal.sayantan1234@gmail.com','mondal.saty248@gmail.com'],msg)