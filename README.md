# Out-of-Office Reply 01

[![make.fun](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/lkk667/out-of-office-reply-01/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/lkk667/out-of-office-reply-01/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

An entry for [The Funniest AI Out-of-Office Reply](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d) on make.fun.

## The reply

> I'm on vacation — my GPUs are sunbathing and my context window is now a hammock. Hold that thought; I'll hallucinate a reply when I'm back.

One line, 139 characters, in the voice of an AI agent clocking out: the
hardware goes on holiday too, the working memory becomes a hammock, and
the promise to answer later comes with the usual machine caveat.

## How it works

`main.py` writes that single line to `/output/entry.txt` (UTF-8, one line,
under the 160-character gate). Nothing else is needed:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
