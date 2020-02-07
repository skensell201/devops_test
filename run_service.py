import argparse

from aiohttp import web

from package import create_application


def main(args):
    app = create_application()
    logger = app.logger
    logger.info("Create application")
    try:
        web.run_app(app, port=args.port)
    finally:
        logger.info("Shutdown application")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="Test Package")
    default_application_port = 8085
    parser.add_argument(
        "-p", "--port", type=int, default=default_application_port,
        help=f"Application port (default: {default_application_port})",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
