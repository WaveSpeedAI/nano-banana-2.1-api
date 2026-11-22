import inspect

import nano_banana_api as api


def _dummy(param):
    ann = str(param.annotation)
    if "List" in ann:
        return ["https://example.com/a"]
    if "int" in ann:
        return 1
    if "float" in ann:
        return 1.0
    if "bool" in ann:
        return True
    return "x"


def test_every_function_sends_only_what_was_given(monkeypatch):
    calls = []

    def fake_run(model, payload, **kwargs):
        calls.append((model, payload, kwargs))
        return {"outputs": ["https://example.com/out"]}

    monkeypatch.setattr(api.wavespeed, "run", fake_run)
    assert set(api.MODELS) == set(api.__all__) - {"MODELS", "upload"}
    for name, model in api.MODELS.items():
        fn = getattr(api, name)
        sig = inspect.signature(fn)
        required = {n: _dummy(p) for n, p in sig.parameters.items() if p.default is inspect.Parameter.empty}
        assert fn(**required) == ["https://example.com/out"]
        got_model, payload, kwargs = calls[-1]
        assert got_model == model
        assert payload == required
        assert kwargs == {"timeout": None, "poll_interval": 1.0}


def test_optional_arguments_are_passed_through(monkeypatch):
    seen = {}
    monkeypatch.setattr(api.wavespeed, "run", lambda model, payload, **kw: seen.update(payload=payload, kw=kw) or {"outputs": []})
    name = next(iter(api.MODELS))
    fn = getattr(api, name)
    sig = inspect.signature(fn)
    everything = {n: _dummy(p) for n, p in sig.parameters.items() if n not in ("timeout", "poll_interval")}
    fn(**everything, timeout=30, poll_interval=2.0)
    assert seen["payload"] == everything
    assert seen["kw"] == {"timeout": 30, "poll_interval": 2.0}
