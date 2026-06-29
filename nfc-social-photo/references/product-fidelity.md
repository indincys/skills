# Product Fidelity Rules

The product reference images are the authority. Do not let visual style rewrite the product.

When multiple product references are present, the current reference image is the authority for only the current prompt. Do not borrow details from other references in the same batch.

## Non-Negotiable Lock

Every prompt must include a product lock block equivalent to:

```text
Product fidelity lock: use the supplied product reference image as the only source for the NFC music card-sleeve charm. Preserve the exact card sleeve silhouette, transparent/colored material, rounded corners, card face, printed image, printed text, card position, keyring hardware, spring rope, star charm, holes, seams, thickness, proportions, and all relative positions. Do not redraw, redesign, simplify, beautify, replace, relabel, recolor, warp, stretch, melt, duplicate, or add logos to the product. Do not change the card artwork, character portrait, typography, accessory shape, or attachment structure.
```

Chinese equivalent:

```text
产品保真锁定：以输入的产品参考图作为 NFC 音乐卡套挂件的唯一设计来源。必须保留卡套轮廓、透明或彩色材质、圆角、卡面、人像或图案、文字、卡片位置、金属钥匙圈、弹簧绳、星形配件、孔位、边线、厚度、比例和所有相对位置。不得重绘、重新设计、简化、美化、替换、改字、改色、拉伸、扭曲、融化、复制产品，也不得新增 logo。不得改变卡面人物、排版、挂件结构或任何小配件形状。
```

For batches, append:

```text
Use only the current reference image for this product. Do not mix in colors, portraits, names, card faces, charms, bells, ropes, clips, or hardware from any other product reference.
```

## What Must Stay Identical

- sleeve outline and rounded corners
- clear or colored sleeve material and edge thickness
- card face, image, text, and internal card placement
- metal ring and connector placement
- spring rope form, curl density, and attachment point
- star charm shape, color, and relative position
- any holes, seams, rivets, borders, clips, or small hardware
- product scale relationship between sleeve, ring, rope, and charm

## Allowed Scene Changes

Allowed:

- real shadows from the product
- mild environmental reflection on plastic
- fingerprints, dust, or tiny surface wear that do not hide or change design
- natural perspective from a believable camera angle
- partial occlusion only when enough product remains visible to verify identity
- direct image generation that integrates the supplied reference product into the scene with matched light, perspective, contact shadows, gravity, and occlusion

Not allowed:

- turning the product into a generic keychain
- replacing the card face with a new person, drawing, album cover, app screen, or logo
- changing star charm position or shape
- turning the spring rope into a ribbon, chain, cable, or strap
- adding typography or stickers directly onto the product
- making the sleeve more luxurious, glossy, metallic, translucent, or thick than the reference
- smoothing away small real details until it looks like a 3D render
- cutting the product out of the reference photo and pasting it onto a separately generated background
- using local compositing as a shortcut for batch generation unless the user explicitly asks for compositing
- borrowing another reference image's colorway, person, name, card face, star charm, bell, spring rope, clip, or hardware

## Prompt Check

Before finalizing, inspect each prompt:

1. Does it name the product as an NFC music card-sleeve charm, keychain, and bag/backpack charm?
2. Does it explicitly say reference image is the only product design source?
3. Does it prohibit redesign, recolor, relabel, warping, and detail changes?
4. Does the scene still allow the product to be clearly visible?
5. Does any style phrase risk changing the product material or making it a rendered object? If yes, rewrite.
6. If there are multiple references, does it explicitly forbid mixing details from other product references?
