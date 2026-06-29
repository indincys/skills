# Output Template

Use Markdown. The default output for one approved product is 24-36 prompt entries. For multiple products, create separate product sections and start with 6-12 pilot prompts per product unless the user explicitly asks for a larger final batch.

Each entry must be long enough to function as a real image-generation brief. Avoid short scene captions.

```markdown
# NFC Social Photo Prompts

Product: NFC music card-sleeve charm / keychain / backpack and bag charm
Aspect ratio: 3:4 vertical
Primary style: realistic social-media atmosphere photography
Batch mode: product-specific prompt sets

## Product A | [Reference filename or id]

### Product Profile

- Dominant colors:
- Card face/person mood:
- Accessory details:
- Best scene families:
- Avoided scene families:
- Fidelity risks:

### Current Product Lock

[One concise product fidelity statement based only on this current product reference. Include no-mixing rule.]

## Prompts

### 01 | [Short Scene Name]

- Visual intention: [What this image should feel like.]
- Social stopping reason: [Why a viewer would pause.]
- Product fit reason: [Why this exact product's color/card/accessories fit this exact scene.]
- Real scene: [Specific lived situation, not an ad scene.]
- Product embedding: [Where the product is, what touches it, how it is used.]
- Light and texture: [Real light source plus imperfections.]
- Composition and camera: [3:4 vertical, viewpoint, crop, focus.]
- Avoid: [No ecommerce, no advertising, no heavy poster, no AI render, no product redesign.]

```prompt
[Final long prompt. Include 3:4 vertical, real photography, product embedding, anti-AI constraints, and the product fidelity lock.]
```

## Product B | [Reference filename or id]

[Repeat profile, current product lock, and prompts. Do not reuse Product A's prompt wording mechanically.]
```

## Prompt Quality Bar

Every final prompt should:

- feel like a photograph from a believable social-media moment
- include 3:4 vertical framing
- include the current product fidelity lock
- include a product fit reason
- forbid mixing details from other product references
- include anti-ad, anti-main-image, anti-heavy-poster, and anti-CGI constraints
- avoid new readable text on non-product props unless exact text is supplied
- specify real light, material, and at least one imperfection
- specify why the product exists in that scene
- avoid generic "beautiful product on table" language

## Good Scene Families

- backpack zipper after class, with locker scratches and afternoon corridor light
- tote handle beside a cafe receipt, mild coffee condensation, soft window light
- bus seat or subway pole, NFC card use implied by transit context
- desk with headphones and playlist glow, product lying beside tangled cable
- bag interior search moment, hand partially lifting strap, product half visible but identifiable
- night rain window, phone screen glow, music mood without neon-ad exaggeration
- campus bench, student ID card, notebook edge, sleeve fabric shadow
- friend's casual phone snapshot, slight motion blur, product hanging naturally from a bag
