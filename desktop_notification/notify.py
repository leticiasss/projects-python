from plyer import notification
from time import sleep

if __name__ == "__main__":
  notification.notify(
    title = "Você foi notificado pelo Python!",
    message = "Testando as notificações feitas pelo plyer",
    app_name = "Your Notify!"
  )

  sleep(4)

