# word-map-api
Takes a word array and returns the synonyms/antonyms related to each.

For example:
```
send:
{
    "words": ["Beautiful", "Cool", "collected"]
}
```
and receive:
```
{
    "beautiful": {
        "antonyms": [
            "ugly"
        ],
        "synonyms": [
            "beautiful"
        ]
    },
    "collected": {
        "antonyms": [
            "spread",
            "uncollected",
            "ungathered"
        ],
        "synonyms": [
            "take_in",
            "call_for",
            "gather_up",
            "collect",
            "hoard",
            "gather",
            "gathered",
            "poised",
            "pick_up",
            "self-possessed",
            "pull_in",
            "amass",
            "roll_up",
            "pile_up",
            "accumulate",
            "pull_together",
            "compile",
            "self-collected",
            "collected",
            "garner",
            "equanimous",
            "self-contained"
        ]
    },
    "cool": {
        "antonyms": [
            "warm",
            "heat"
        ],
        "synonyms": [
            "cool_off",
            "cool",
            "aplomb",
            "poise",
            "nerveless",
            "sang-froid",
            "coolheaded",
            "chill",
            "cool_down",
            "assuredness"
        ]
    }
}
```