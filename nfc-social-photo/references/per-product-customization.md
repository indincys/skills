# Per-Product Customization

The highest-quality outputs come from treating every reference image as a different product with its own visual personality. Do not create one generic scene list and apply it to all products.

## Product Profile First

Before writing prompts for a product, create a short profile:

- Reference id or filename
- Dominant colors and material finish
- Card face/person mood and visible text style
- Accessories: spring rope color, star charm colors, bell, clip, keyring, small stickers, holes, seams
- Likely user and social context
- Best scene families
- Scene families to avoid
- Product-specific fidelity risks

Example profile logic:

```text
Green product: fresh campus feeling, green coiled rope, green/translucent star charms, light schoolbag and locker scenes fit well. Avoid nightclub neon, luxury black styling, and heavy coffee-brown scenes.
Yellow product: warm, bright, cafe and convenience-store scenes fit well; receipt, cup condensation, afternoon window light, and friends' table moments can support the color. Avoid cold rainy scenes as the main direction.
Blue product: cool, clean, commute, bag-interior, rainy window, transit, and overcast daylight scenes fit well. Avoid warm yellow cafe scenes unless there is a clear contrast reason.
```

## Prompt Generation Rule

For multiple product references:

1. Analyze Product A.
2. Write Product A's own prompt set.
3. Analyze Product B from scratch.
4. Write Product B's own prompt set.
5. Continue product by product.

Do not write 30 generic prompts first and then apply them to A/B/C/D/E.

Scene families may overlap, but the prompt must be rewritten around the current product. A green campus zipper prompt, a yellow cafe receipt prompt, and a blue bag-search prompt should not share the same wording except for product-fidelity language.

## Required Fit Reason

Every prompt must include a fit reason:

```text
Product fit reason: this scene uses the current product's [color/accessory/card mood] because [specific visual or social reason].
```

If the fit reason sounds generic, rewrite the scene. If the same fit reason could apply to every product, it is not product-specific enough.

## Anti-Mixing Rule

Every product-specific prompt must say that the model should not borrow details from other references:

```text
Use only the current reference image for this product. Do not mix in colors, portraits, names, card faces, charms, bells, ropes, clips, or hardware from any other product reference.
```

This matters when the batch includes many similar card-sleeve charms. Without the rule, image generation can blend colorways and accessories across references.

## Quality Workflow

Default high-quality workflow:

1. Generate 6-12 pilot prompts per product.
2. Direct-generate 2-3 images for the product using the strongest prompts.
3. Inspect product fidelity, physical contact, lighting, scene fit, and social-media realism.
4. Only expand to 24-36 prompts after the pilot passes.

For large batches, warn that quality drops if the process becomes mechanical. Recommend fewer, stronger prompts per product rather than one universal scene matrix.
