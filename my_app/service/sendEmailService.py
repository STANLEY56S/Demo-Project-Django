
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Method to use the formate content using the Data That GIven file path can be html or txt
def render_sting(txt_path, content:dict):
    # render the content.
    return render_to_string(
        txt_path,
        context=content,
    )

def create_email_multi_alternatives(data):
    # Then, create a multipart email instance.
    msg = EmailMultiAlternatives(
        data["subject"],
        data["content"],
        data["from"],
        data["recipient_list"],
        headers={"List-Unsubscribe": "<mailto:unsub@example.com>", **data['header']},
    )

    return msg

def service_send_email(data):
    try:
        # create send email message object
        msg = create_email_multi_alternatives(data)

        # Lastly, attach the HTML content to the email instance and send.
        msg.attach_alternative(data['content'], data['content_type'])
        msg.send()
        
    except Exception as e:
        print("error",e)