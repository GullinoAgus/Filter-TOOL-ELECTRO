import sys, logging
import app


def main():
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    aplicacion = app.QtWidgets.QApplication(sys.argv)
    ventana = app.MainWindow()
    ventana.show()
    sys.exit(aplicacion.exec())


if __name__ == "__main__":
    main()

