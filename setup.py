from setuptools import setup

setup(
    name="scripts",
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "populate_db=scripts.populate_db:entrypoint",
        ]
    },
)
