# platform_id = 62920b3c835b11efb3adef86
# module_id = 62920b63835b11efb3adef89
# action_id = 62920b8e835b11efb3adef8c
# group_action_id = 62920f4f835b11efb3adef90
# admin_group_id = 62932880cf2c7f4d9a7ea93b
# user_group_id = 629206e4835b11efb3adef81
import uvicorn
from fastapi import FastAPI, BackgroundTasks
from send_mail import send_email_background, send_email_async
app = FastAPI(title='How to Send Email')


@app.get('/')
def index():
    return 'Hello World'



@app.get('/send-email/asynchronous')
async def send_email_asynchronous():
    await send_email_async('Hello World','mdfahadhossain71@gmail.com',
    {'title': 'Hello World', 'name': 'John Doe'})
    return 'Success'

@app.get('/send-email/backgroundtasks')
def send_email_backgroundtasks(background_tasks: BackgroundTasks):
    send_email_background(background_tasks, 'Hello World',   
    'mdfahadhossain71@gmail.com', {'title': 'Hello World', 'name':       'John Doe'})
    return 'Success'

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)