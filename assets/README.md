# Profile assets

## Identity

`hero-v3-compact.svg` is the desktop master (960 × 168).
`hero-v3-mobile.svg` is the narrow layout (480 × 168), selected by the README
`picture` element at a viewport width of 600px or less.

Both use live SVG text with system font fallbacks. Keep their wording and palette
in sync. Edit `#profile-name`, `#profile-fields`, `#identity-mark`, `#background`,
and `#accent` directly. Colours switch with `prefers-color-scheme`; each palette
has its own opaque background so the artwork remains legible on either GitHub theme.
The only identity accent is #E34432. The hero is deliberately static.

## Toolbox sources

All displayed images are local SVGs. Logo geometry is retained; the `monochrome`
SVG filter removes saturation without replacing brand shapes. OpenAI and Bonsai
already use monochrome paths. The README alt text identifies every tool.

- `toolbox-languages.svg`: [Skill Icons](https://skillicons.dev/icons?i=python,c,dart,flutter,swift,kotlin,ts,js,lua,nextjs&perline=10)
- `toolbox-platform.svg`: [Skill Icons](https://skillicons.dev/icons?i=firebase,supabase,vercel,cloudflare,gcp,docker,git,github,figma&perline=9)
- Skill Icons is MIT licensed; the upstream notice is in `LICENSE.skill-icons`.
- `huggingface-logo.svg`: [Hugging Face](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)
- `gemini-logo.svg`: [Simple Icons](https://cdn.simpleicons.org/googlegemini), [CC0](https://github.com/simple-icons/simple-icons/blob/develop/LICENSE.md).
- OpenAI, Qwen, Bonsai AI and Ghostty reuse the existing repository assets.

Downloaded assets were already used remotely by this README; these copies remove
that runtime dependency. The Skill Icons platform strip includes two embedded PNG
textures from upstream; they do not make network requests. Product names and logos remain their owners' marks.

## Activity

`../profile-3d-contrib/profile-night-rainbow.svg` and its generation workflow are
maintained independently. Do not rescale individual bars, replace contribution
data, or change the shockwave animation when editing the identity artwork.
