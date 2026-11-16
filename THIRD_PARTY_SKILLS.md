# Skills in this repository that come from other projects

These skill folders under `.claude/skills/` are copied unchanged from their
projects. To update one, copy the folder again from a newer commit and change
the commit below.

| Skills | From | Commit | Licence |
|---|---|---|---|
| `earshot` | [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot) `skills/earshot` | `4ac3d2a` | MIT (`.claude/skills/earshot/LICENSE`) |
| `remotion-best-practices`, `remotion-captions`, `remotion-create`, `remotion-docs`, `remotion-interactivity`, `remotion-license`, `remotion-maps`, `remotion-markup`, `remotion-multimedia`, `remotion-render`, `remotion-saas`, `remotion-studio`, `remotion-upgrade` | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) `packages/skills/skills` | `b0c3781` | Remotion License (`third-party-licenses/remotion-LICENSE.md`) |
| `hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `media-use`, `figma`, `slideshow`, `style-sampling`, `reverse-any-video`, `remotion-to-hyperframes` | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) `skills` | `c06e98e` | Apache 2.0 (`third-party-licenses/hyperframes-LICENSE`) |

Notes:

- Remotion is free for individuals and small companies; larger for-profit
  companies need a paid company licence. The `remotion-license` skill has the
  details.
- The HyperFrames command and its `media-use` scripts send usage statistics to
  HeyGen (PostHog) unless `HYPERFRAMES_NO_TELEMETRY=1` or `DO_NOT_TRACK=1` is
  set. Some `media-use` features call paid services (HeyGen, ElevenLabs,
  Gemini) and only work with the owner's own API keys.
- `learn-style` is the owner's own skill, not third-party.
