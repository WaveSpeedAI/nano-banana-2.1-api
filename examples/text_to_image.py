"""Nano Banana 2.1 — text-to-image with `google/nano-banana-2.1/text-to-image`.

export WAVESPEED_API_KEY first: https://wavespeed.ai/accesskey
"""
import nano_banana_api

urls = nano_banana_api.text_to_image(
    prompt="A lighthouse on a rocky coast at dawn, soft golden light, long exposure",
)
print(urls[0])
