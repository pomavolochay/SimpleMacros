import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Конфигурационные параметры
DELAY = 0.001
BUTTON = Button.right
START_STOP_KEY = KeyCode(char='a')
STOP_KEY = KeyCode(char='b')


class ClickMouse(threading.Thread):
    """Класс-поток для автоматического кликания мышью."""

    def __init__(self, delay: float, button: Button) -> None:
        """
        Инициализация потока.
        
        :param delay: Задержка между кликами в секундах
        :param button: Кнопка мыши для клика
        """
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        self.mouse = Controller()  # Инициализация контроллера мыши

    def start_clicking(self) -> None:
        """Запуск автоматического кликания."""
        self.running = True

    def stop_clicking(self) -> None:
        """Остановка автоматического кликания."""
        self.running = False

    def exit(self) -> None:
        """Полная остановка программы."""
        self.stop_clicking()
        self.program_running = False

    def run(self) -> None:
        """
        Основной цикл потока.
        Выполняет клики пока program_running = True.
        Активные клики происходят только когда running = True.
        """
        while self.program_running:
            while self.running:
                self.mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)  # Короткая пауза при простое


def on_press(key: KeyCode) -> None:
    """
    Обработчик нажатия клавиш.
    
    :param key: Клавиша, которая была нажата
    """
    if key == START_STOP_KEY:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == STOP_KEY:
        click_thread.exit()
        listener.stop()


if __name__ == "__main__":
    # Создание и запуск потока с автокликом
    click_thread = ClickMouse(DELAY, BUTTON)
    click_thread.start()

    # Запуск слушателя клавиатуры
    with Listener(on_press=on_press) as listener:
        listener.join()