import eel

def run():
    eel.init('src')

    @eel.expose
    def linking(link):
        print('mira un link xd: '+link)
        return f"xx{link}xx"

    eel.start('index.html', size=(400, 400), port=8080)


if __name__ == '__main__':
    run()