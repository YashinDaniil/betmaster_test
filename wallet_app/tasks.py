from wallet_app.services.superpay_api import SuperPayApi


@shared_task
def get_deposit_data():
    super_pay = SuperPayApi()
    super_pay.get_callback
    #Записать в бд и завершить таску, если api отработало
