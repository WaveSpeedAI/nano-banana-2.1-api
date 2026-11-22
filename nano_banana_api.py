"""Nano Banana 2.1 API — Python wrapper for the WaveSpeedAI hosted endpoints.

Each function calls one endpoint through the official `wavespeed` SDK, waits for
the result and returns the list of output URLs. Arguments left as None are not
sent, so the server-side defaults apply.

Set WAVESPEED_API_KEY first: https://wavespeed.ai/accesskey

Generated from the live model schemas; do not edit by hand.
"""
from typing import Any, Dict, List, Optional

import wavespeed

__version__ = "0.1.0"

__all__ = ["MODELS", "upload", "text_to_image", "edit"]

#: function name -> WaveSpeedAI model id
MODELS: Dict[str, str] = {
    "text_to_image": "google/nano-banana-2.1/text-to-image",
    "edit": "google/nano-banana-2.1/edit",
}


def upload(file: Any) -> str:
    """Upload a local file (path or binary file object) and return its URL."""
    return wavespeed.upload(file)


def _run(name: str, params: Dict[str, Any], timeout: Optional[float], poll_interval: float) -> List[str]:
    payload = {k: v for k, v in params.items() if v is not None}
    result = wavespeed.run(MODELS[name], payload, timeout=timeout, poll_interval=poll_interval)
    return list(result["outputs"])


def text_to_image(
    prompt: str,
    *,
    aspect_ratio: Optional[str] = None,
    resolution: Optional[str] = None,
    enable_web_search: Optional[bool] = None,
    enable_image_search: Optional[bool] = None,
    output_format: Optional[str] = None,
    timeout: Optional[float] = None,
    poll_interval: float = 1.0,
) -> List[str]:
    """Google's Nano Banana 2.1 is the latest Nano Banana text-to-image model, with gains in visual design, subject consistency and prompt adherence, 1K to 4K output and optional web search grounding.

    Model: ``google/nano-banana-2.1/text-to-image``

    Args:
        prompt: The positive prompt for the generation.
        aspect_ratio: The aspect ratio of the generated image. Defaults to 1:1. Allowed: 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9, 1:4, 4:1, 1:8, 8:1. Server default: "1:1".
        resolution: The resolution of the output image. Allowed: 1k, 2k, 4k. Server default: "1k".
        enable_web_search: If enabled, the model will use web search to enhance the generation with real-time information. Server default: false.
        enable_image_search: If enabled, the model will use image search to enhance the generation with real-time information. Server default: false.
        output_format: The format of the output image. Allowed: png, jpeg. Server default: "png".
        timeout: Maximum seconds to wait for the result (None = no limit).
        poll_interval: Seconds between status checks.

    Returns:
        List of output URLs.
    """
    return _run(
        "text_to_image",
        {"prompt": prompt, "aspect_ratio": aspect_ratio, "resolution": resolution, "enable_web_search": enable_web_search, "enable_image_search": enable_image_search, "output_format": output_format},
        timeout,
        poll_interval,
    )


def edit(
    prompt: str,
    images: List[str],
    *,
    aspect_ratio: Optional[str] = None,
    resolution: Optional[str] = None,
    enable_web_search: Optional[bool] = None,
    enable_image_search: Optional[bool] = None,
    output_format: Optional[str] = None,
    timeout: Optional[float] = None,
    poll_interval: float = 1.0,
) -> List[str]:
    """Google Nano Banana 2.1 Edit is the latest Nano Banana image editing model, with gains in visual design, subject consistency and prompt adherence, up to 14 reference images and 1K to 4K output.

    Model: ``google/nano-banana-2.1/edit``

    Args:
        prompt: The positive prompt for the generation.
        images: List of URLs of input images for editing. The maximum number of images is 14. Allowed: up to 14 items.
        aspect_ratio: The aspect ratio of the generated image. If not specified, it is determined automatically from the input image. Allowed: 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9, 1:4, 4:1, 1:8, 8:1.
        resolution: The resolution of the output image. Allowed: 1k, 2k, 4k. Server default: "1k".
        enable_web_search: If enabled, the model will use web search to enhance the generation with real-time information. Server default: false.
        enable_image_search: If enabled, the model will use image search to enhance the generation with real-time information. Server default: false.
        output_format: The format of the output image. Allowed: png, jpeg. Server default: "png".
        timeout: Maximum seconds to wait for the result (None = no limit).
        poll_interval: Seconds between status checks.

    Returns:
        List of output URLs.
    """
    return _run(
        "edit",
        {"prompt": prompt, "images": images, "aspect_ratio": aspect_ratio, "resolution": resolution, "enable_web_search": enable_web_search, "enable_image_search": enable_image_search, "output_format": output_format},
        timeout,
        poll_interval,
    )
