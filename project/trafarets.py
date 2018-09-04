from functools import partial

import trafaret as t
from trafaret.contrib.object_id import MongoId

NotEmptyString = partial(t.String, min=1)

GetTagsTrafaret = t.Dict({
    t.Key("text"): t.String
})

TagsOutputTrafaret = t.Dict({
    t.Key("tags"): t.List(t.Dict({
        t.Key("_id"): MongoId() >> str,
        t.Key("tag"): t.String(),
    }), min_length=1),
})
