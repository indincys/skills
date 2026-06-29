---
name: nfc-social-photo
description: Manual invocation only. Use this skill only when the user explicitly names nfc-social-photo or asks to use this exact skill for NFC music card-sleeve charms, keychains, backpack charms, bag charms, and similar card-holder pendant product references that need product-specific realistic social-media atmosphere image prompts with strict fidelity.
---

# NFC Social Photo

## Overview

Manual invocation only: do not use this skill unless the user explicitly asks for `nfc-social-photo` by name or clearly says to use this exact skill.

Use this skill to create long, specific image-generation prompts for real-life atmosphere product visuals. The goal is a social-media image that feels worth pausing on: a believable lifestyle moment, tactile light, lived-in surfaces, and a product that remains exactly the same as the supplied reference.

This skill is for product scene images, mood assets, social posts, seed images for image-to-video, and creative prompt batches. It is not for ecommerce white-background images, promotion posters, banner ads, or redesigning the product.

## Required References

Before writing prompts, read:

- `references/product-fidelity.md`
- `references/social-photo-method.md`
- `references/per-product-customization.md`
- `references/output-template.md`

Also read `references/xiaoxiaodong-research.md` when the user asks for prompts influenced by xiaoxiaodong, long-form prompt craft, social-media stopping power, or when refreshing the style method.

## Workflow

1. Treat each reference image as its own product, not as an interchangeable variant. Never make one universal scene pool and apply it mechanically to every product.
2. For each product reference image, write a short product profile before writing prompts: colorway, card face/person, printed details, accessory set, hardware, mood, likely user, best scene families, and scene families to avoid.
3. Generate product-specific scene directions from that profile. Green, yellow, blue, pink, dark, transparent, cute, cool, campus, commute, cafe, or night products should not receive identical 30-scene lists.
4. Convert the product into a real-life use situation before choosing any visual style. Ask: who has this exact product, where is it hanging or lying, what just happened, why would someone photograph it now?
5. Build each prompt as a photography brief, not a slogan. Start with the true moment, then specify product placement, nearby objects, light behavior, camera position, realistic imperfections, composition motive, product-fit reason, and social-media stopping reason.
6. Include a current-reference product lock block in every prompt. The image model must use the current product reference as the only product design source and must not mix in colors, characters, card faces, charms, ropes, bells, text, or hardware from other references.
7. Keep the default batch focused: for multiple product references, first create 6-12 pilot prompts per product and suggest direct image-generation tests before expanding. For an approved single product, 24-36 prompts is acceptable.
8. Save the result as Markdown and run `scripts/validate_prompt_file.py` on it before handing it over.

## Image Generation Execution Rule

When the user asks to generate images from these prompts, each final image must be generated directly with the product reference image and the scene prompt in the same image-generation call. Do not generate empty scene backgrounds first and then cut out or paste the product into them.

For batch work, use this direct pattern:

```text
Input image role: this product reference image is the only product appearance source.
Task: generate the same product physically integrated into this real scene.
Requirement: match lighting, perspective, contact shadows, occlusion, gravity, and material interaction during generation.
Do not use the product as a pasted cutout, sticker, overlay, or separate composited layer.
```

If direct generation is too slow or too many images are requested, report the cost/time tradeoff and ask whether to reduce the batch size. Never silently switch to local cutout compositing, because it destroys the real photographic contact this skill is designed to create.

## Style Rules

- Lead with real photography: natural light, mixed indoor light, phone-camera perspective, shallow but plausible depth of field, visible shadows, slight dust, small wrinkles, fingerprints, scuffs, fabric texture, table marks, and imperfect object spacing.
- Create a social pause through human context, not through advertising pressure. The product should feel discovered in a moment someone would share.
- Let the product have a relationship with the scene: attached to a moving bag, half caught in a zipper pull, beside a transit card, tangled with earphones, resting on a coffee receipt, or pressed against a locker door.
- Make the scene prove why it belongs to the current product. A prompt must explain why this colorway, portrait/card mood, rope, charm, bell, or hardware fits the chosen place and light.
- Keep graphics minimal. Small stickers, notes, lock-screen glow, or paper scraps are acceptable only when they feel physically present.
- Avoid adding new readable text on scene props. Non-product receipts, cards, screens, notes, books, and labels should be cropped, blurred, folded, or too small to read unless the user explicitly asks for exact text.
- Use 3:4 vertical framing by default and write it explicitly in every prompt.

## Hard Prohibitions

Do not create prompts that request:

- ecommerce main image, white-background upgrade, isolated packshot, catalog layout, banner ad, promotion poster, hard-selling copy, price tag, coupon, CTA button, or campaign key visual
- heavy poster design, giant typography over the product, magazine cover treatment, dense graphic overlays, surreal ad set, impossible prop pile, or luxury studio staging
- over-polished commercial retouching, mirror-perfect plastic, fake reflections, excessive sharpness, hyper-clean CGI, 3D render, cartoonization, or illustration conversion
- any product redesign, changed color, changed card artwork, changed text, changed hardware, changed star charm, changed rope, changed proportions, changed material, or new logo/label
- background-only generation followed by product cutout compositing, pasted product overlays, sticker-like insertion, or any workflow where product lighting, perspective, gravity, occlusion, and contact shadows are not solved by the image model in one direct generation
- one generic prompt set applied to all product references without per-product product profiles and per-prompt fit reasons
- cross-product mixing, such as using one product's color, portrait, card text, star charm, bell, rope, or hardware in another product's prompt

## Output Contract

Use `references/output-template.md` as the structure. Each prompt should contain:

- visual intention
- social-media stopping reason
- current product profile
- product-fit reason
- real scene
- product embedding
- light and texture
- composition and camera
- anti-AI and anti-ad constraints
- product fidelity lock
- final prompt text

Run:

```bash
python3 scripts/validate_prompt_file.py path/to/output.md
```

For a 12-prompt forward-test:

```bash
python3 scripts/validate_prompt_file.py path/to/output.md --min-prompts 12 --max-prompts 12
```
