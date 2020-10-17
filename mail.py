import email
import imaplib
import os
svdir = 'e:/desafio'
EMAIL = 'automacao@trackcash.com.br'
PASSWORD = 'mudar!@#'
SERVER = 'trackcash.com.br'

mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)
mail.select('inbox')
status, data = mail.search(None, '(SUBJECT "Planilha de Repasse" )')
mail_ids = []
for block in data:
    mail_ids += block.split()
for i in mail_ids:
    status, data = mail.fetch(i, '(RFC822)')
    for response_part in data:
        if isinstance(response_part, tuple):
            message = email.message_from_bytes(response_part[1])
            mail_from = message['from']
            mail_subject = message['subject']
            if message.is_multipart():
                mail_content = ''
                for part in message.get_payload():
                    if part.get_content_type() == 'text/plain':
                        mail_content += part.get_payload()

            else:
                mail_content = message.get_payload()
            filename = part.get_filename()
            if filename is not None:
                sv_path = os.path.join(svdir, filename)
                if not os.path.isfile(sv_path):
                    print(sv_path)
                    fp = open(sv_path, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
            content_type = part.get_content_type()