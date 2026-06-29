# Social Photo Method

This method converts a product reference into realistic atmosphere photography for social media. The image should feel like a good creator casually found a beautiful moment, not like a brand asked for an ad.

## Core Principle

The product is not "displayed"; it is caught inside a lived moment. Every scene must answer:

- Why is the product here?
- What touched it, carried it, or was used with it?
- What light existed in that place?
- What small imperfection proves the moment is real?
- Why would a viewer pause for more than one second?

For actual image generation, the product and scene must be solved together in the same generation. A pasted cutout can preserve pixel details, but it usually fails the main goal: believable contact, gravity, occlusion, light direction, and phone-photo realism.

When there are multiple product references, the scene must be chosen for the current product's color, accessories, card face, and mood. Reusing the same scene prompt across every product makes the result feel generic.

## Scene Mechanics

Use one clear mechanism per prompt:

- Hanging in use: attached to a backpack zipper, tote handle, schoolbag strap, keychain cluster, locker hook, or bike key.
- Found on a surface: cafe table, desk, music corner, bus seat, classroom bench, bedside shelf, checkout counter, or transit station ledge.
- Mid-action: hand searching inside a bag, card being tapped, strap being lifted, earphones being untangled, keys being dropped, friend holding the charm for a quick photo.
- Occluded discovery: product half seen through a bag opening, behind a coffee cup, near a folded sleeve, under a receipt, or partly hidden by headphones.
- Night mood: phone screen glow, window reflection, bus interior light, bedside lamp, neon spill, rainy glass, or low music-room light.
- Day mood: soft window light, campus afternoon, cafe shade, morning commute, desk sunlight, or overcast outdoor light.

## Composition Rules

- Use 3:4 vertical framing by default.
- Place the product where a phone camera could naturally find it: lower third, side edge, hanging near the top corner, or slightly off-center.
- Avoid perfect symmetry unless the scene itself explains it.
- Include enough surrounding context to prove use, but not so many props that the scene becomes a styled advertisement.
- Use crop and foreground only when they feel photographic: table edge, sleeve, bag mouth, strap, window frame, locker door, cup rim.
- Keep non-product text physically present but unreadable. Receipts, transit cards, notebooks, phone screens, locker timetables, and labels should be folded, cropped, blurred, dim, or too small to read unless the user provides exact text.

## Light And Texture

Prefer:

- natural window light with soft falloff
- mixed indoor light with mild color cast
- soft phone-screen glow
- cafe ambient light, bus light, corridor light, bedside lamp, or rainy-window diffusion
- real shadows under the product
- tiny scuffs, lint, fingerprints, dust, wrinkles, scratches, table marks, paper fibers, fabric texture, zipper scratches, and worn metal

Avoid:

- perfect studio light
- unreal rim light
- glossy CGI reflections
- plastic-perfect surfaces
- excessive sharpening
- fake bokeh that ignores distance
- spotless prop styling
- crisp invented text on receipts, screens, cards, labels, or notebooks

## Social-Media Stopping Power

A prompt should include one reason the image is worth pausing on:

- It feels like a private routine: music before class, commute playlist, night walk, bag check before leaving.
- It has a tactile object relationship: NFC music charm plus earphones, transit card, student ID, receipt, keys, coffee lid, or locker.
- It contains a small narrative hook: "someone just changed the playlist", "the card was grabbed in a rush", "a friend noticed the charm on a bag".
- It has believable sensory texture: quiet light, worn fabric, small scratches, rain, table condensation, cable tangles.
- It leaves room for imagination rather than shouting a product claim.

## Language Pattern

Write each final prompt in this order:

1. "Use the supplied product reference photo as the only product design source."
2. Scene moment and observer viewpoint.
3. Exact product embedding and surrounding object relationship.
4. Light, material, and imperfections.
5. Composition, camera, lens feel, depth of field.
6. Social-media stopping reason.
7. Negative constraints against ad/poster/ecommerce/AI look.
8. Product-fidelity lock.

## Anti-Advertising Filter

If a prompt could be used as a homepage hero, product launch poster, banner, or polished main product image, rewrite it. Add real-life context, weaker selling pressure, more ordinary surroundings, and less design dominance.
