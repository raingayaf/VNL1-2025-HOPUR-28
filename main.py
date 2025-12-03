from ui.uimain import UIMain


def build_app() -> UIMain:
    app: UIMain = UIMain()
    return app


def main() -> None:
    app: UIMain = build_app()
    app.run()


if __name__ == "__main__":
    main()
