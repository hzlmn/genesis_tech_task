def setup_main_handler(app, handler):
    app.router.add_post(
        "/get_tags",
        handler.get_tags,
        name="get_tags",
    )
