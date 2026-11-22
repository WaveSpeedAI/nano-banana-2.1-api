# Nano Banana 2.1 API — Python wrapper

Call **Nano Banana 2.1** from Python with one function per endpoint: text-to-image, image editing. Built on the official [`wavespeed`](https://github.com/WaveSpeedAI/wavespeed-python) SDK and the [WaveSpeedAI](https://wavespeed.ai/?utm_source=github&utm_medium=readme&utm_campaign=nano-banana-2.1-api) hosted API — no GPU, pay per generation.

<p>
  <a href="https://wavespeed.ai/nano-banana-2-1-api?utm_source=github&utm_medium=readme&utm_campaign=nano-banana-2.1-api"><img src="https://img.shields.io/badge/Nano_Banana_2.1_API-Get_API_key-00E5FF?style=for-the-badge&labelColor=0B0B0F" alt="Nano Banana 2.1 API"></a>
  <a href="https://wavespeed.ai/image-generator?utm_source=github&utm_medium=readme&utm_campaign=nano-banana-2.1-api"><img src="https://img.shields.io/badge/No_code-Try_in_browser-7C3AED?style=for-the-badge&labelColor=0B0B0F" alt="Try in browser"></a>
</p>

- **Nano Banana 2.1 API guide, live pricing and playground:** [wavespeed.ai/nano-banana-2-1-api](https://wavespeed.ai/nano-banana-2-1-api?utm_source=github&utm_medium=readme&utm_campaign=nano-banana-2.1-api)
- **No code:** generate in the browser with the [AI Image Generator](https://wavespeed.ai/image-generator?utm_source=github&utm_medium=readme&utm_campaign=nano-banana-2.1-api) on WaveSpeedAI

## Quick start

```bash
pip install git+https://github.com/WaveSpeedAI/nano-banana-2.1-api.git
export WAVESPEED_API_KEY="your-api-key"   # https://wavespeed.ai/accesskey
```

```python
import nano_banana_api

urls = nano_banana_api.text_to_image(
    prompt="A lighthouse on a rocky coast at dawn, soft golden light, long exposure",
)
print(urls[0])
```

Every function waits for the generation to finish and returns a list of output URLs. Optional arguments you leave out are not sent, so the API defaults apply. Inputs such as images, videos and audio are passed as URLs; use `nano_banana_api.upload("local-file")` to get a URL for a local file.

## Endpoints

| Function | Model | Type |
| - | - | - |
| [`text_to_image()`](#text_to_image) | [google/nano-banana-2.1/text-to-image](https://wavespeed.ai/models/google/nano-banana-2.1/text-to-image?utm_source=github&utm_medium=readme&utm_campaign=nano-banana-2.1-api) | text-to-image |
| [`edit()`](#edit) | [google/nano-banana-2.1/edit](https://wavespeed.ai/models/google/nano-banana-2.1/edit?utm_source=github&utm_medium=readme&utm_campaign=nano-banana-2.1-api) | image-to-image |

Each model page has a playground, live pricing and copy-paste API snippets. Prices are per generation and depend on the settings you choose; check a request before running it with `wavespeed price <model>` from the [CLI](https://github.com/WaveSpeedAI/wavespeed-cli).

## Parameters

### text_to_image

`google/nano-banana-2.1/text-to-image` — Google's Nano Banana 2.1 is the latest Nano Banana text-to-image model, with gains in visual design, subject consistency and prompt adherence, 1K to 4K output and optional web search grounding.

| Parameter | Type | Required | Default | Allowed | Description |
| - | - | - | - | - | - |
| `prompt` | str | yes |  |  | The positive prompt for the generation. |
| `aspect_ratio` | str |  | `"1:1"` | `1:1`, `3:2`, `2:3`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`, `1:4`, `4:1`, `1:8`, `8:1` | The aspect ratio of the generated image. Defaults to 1:1. |
| `resolution` | str |  | `"1k"` | `1k`, `2k`, `4k` | The resolution of the output image. |
| `enable_web_search` | bool |  | `false` |  | If enabled, the model will use web search to enhance the generation with real-time information. |
| `enable_image_search` | bool |  | `false` |  | If enabled, the model will use image search to enhance the generation with real-time information. |
| `output_format` | str |  | `"png"` | `png`, `jpeg` | The format of the output image. |

### edit

`google/nano-banana-2.1/edit` — Google Nano Banana 2.1 Edit is the latest Nano Banana image editing model, with gains in visual design, subject consistency and prompt adherence, up to 14 reference images and 1K to 4K output.

| Parameter | Type | Required | Default | Allowed | Description |
| - | - | - | - | - | - |
| `prompt` | str | yes |  |  | The positive prompt for the generation. |
| `images` | List[str] | yes |  | up to 14 items | List of URLs of input images for editing. The maximum number of images is 14. |
| `aspect_ratio` | str |  |  | `1:1`, `3:2`, `2:3`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`, `1:4`, `4:1`, `1:8`, `8:1` | The aspect ratio of the generated image. If not specified, it is determined automatically from the input image. |
| `resolution` | str |  | `"1k"` | `1k`, `2k`, `4k` | The resolution of the output image. |
| `enable_web_search` | bool |  | `false` |  | If enabled, the model will use web search to enhance the generation with real-time information. |
| `enable_image_search` | bool |  | `false` |  | If enabled, the model will use image search to enhance the generation with real-time information. |
| `output_format` | str |  | `"png"` | `png`, `jpeg` | The format of the output image. |

## REST and CLI

The wrapper is a thin layer over the REST API: submit, then poll for the result.

```bash
curl -s -X POST "https://api.wavespeed.ai/api/v3/google/nano-banana-2.1/text-to-image" \
  -H "Authorization: Bearer $WAVESPEED_API_KEY" -H "Content-Type: application/json" \
  -d '{"prompt": "A lighthouse on a rocky coast at dawn, soft golden light, long exposure"}'
# -> {"data": {"id": "<prediction_id>"}}

curl -s "https://api.wavespeed.ai/api/v3/predictions/<prediction_id>/result" \
  -H "Authorization: Bearer $WAVESPEED_API_KEY"
# -> status: completed, outputs: ["<url>"]
```

```bash
npm i -g @wavespeed/cli && wavespeed login
wavespeed run google/nano-banana-2.1/text-to-image -p "your prompt"
```

## Related

- [awesome-nano-banana-api](https://github.com/WaveSpeedAI/awesome-nano-banana-api) — prompt library and variant guide
- More model wrappers: [Seedance 2.5](https://github.com/WaveSpeedAI/seedance-2.5-api) · [Wan 3.0](https://github.com/WaveSpeedAI/wan-3.0-api) · [Kling 4.0](https://github.com/WaveSpeedAI/kling-4.0-api) · [Veo 3.1](https://github.com/WaveSpeedAI/veo-3.1-api) · [MiniMax H3](https://github.com/WaveSpeedAI/minimax-h3-api) · [HappyHorse 1.1](https://github.com/WaveSpeedAI/happyhorse-1.1-api) · [FLUX 3](https://github.com/WaveSpeedAI/flux-3-api) · [Seedream 5.5](https://github.com/WaveSpeedAI/seedream-5.5-api) · [GPT Image 2.6](https://github.com/WaveSpeedAI/gpt-image-2.6-api)
- SDKs and tools: [Python](https://github.com/WaveSpeedAI/wavespeed-python) · [JavaScript](https://github.com/WaveSpeedAI/wavespeed-javascript) · [CLI](https://github.com/WaveSpeedAI/wavespeed-cli) · [MCP server](https://github.com/WaveSpeedAI/mcp-server) · [ComfyUI nodes](https://github.com/WaveSpeedAI/wavespeed-comfyui)
- [Full model catalog](https://wavespeed.ai/models?utm_source=github&utm_medium=readme&utm_campaign=nano-banana-2.1-api)

## Notes

- Nano Banana 2.1 is a model by Google. This repository is maintained by WaveSpeedAI and wraps the WaveSpeedAI hosted API for it.
- Function signatures and the tables above are generated from the live model schemas (last generated 2026-11-22). The model pages are the source of truth if an endpoint changes.
- Issues and pull requests are welcome. License: MIT.
