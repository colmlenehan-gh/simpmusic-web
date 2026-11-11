#!/usr/bin/env python3
"""Convert the original SimpIcons ImageVector path commands to SVG without redrawing them.
Usage: python3 scripts/port-icons.py /path/to/SimpMusic
"""
import sys,re,json
from pathlib import Path
root=Path(sys.argv[1])/'composeApp/src/commonMain/kotlin/com/maxrave/simpmusic/ui/icon'
names={'home':'Home','search':'Search','library':'LibraryMusic','play':'PlayArrow','pause':'Pause','previous':'SkipPrevious','next':'SkipNext','shuffle':'Shuffle','repeat':'Repeat','repeatOne':'RepeatOne','heart':'Favorite','heartOutline':'FavoriteBorder','more':'MoreVert','settings':'Settings','person':'Person','add':'Add','close':'Close','history':'History','analytics':'TrendingUp','queue':'FormatListBulleted','panel':'PictureInPictureAlt','mix':'Sensors','download':'Download','music':'MusicNote','back':'ArrowBack','logout':'Logout','sync':'Sync'}
commands={'moveTo':'M','moveToRelative':'m','lineTo':'L','lineToRelative':'l','horizontalLineTo':'H','horizontalLineToRelative':'h','verticalLineTo':'V','verticalLineToRelative':'v','quadTo':'Q','quadToRelative':'q','reflectiveQuadTo':'T','reflectiveQuadToRelative':'t','curveTo':'C','curveToRelative':'c','reflectiveCurveTo':'S','reflectiveCurveToRelative':'s','arcTo':'A','arcToRelative':'a','close':'Z'}
result={}
for key,name in names.items():
 p=root/(name+'.kt')
 if not p.exists():continue
 src=p.read_text();paths=[]
 for block in re.findall(r'path\([\s\S]*?\)\s*\{([\s\S]*?)\n\s*\}',src):
  parts=[]
  for cmd,args in re.findall(r'\b('+ '|'.join(commands)+r')\(([^)]*)\)',block):
   values=[v.strip().removesuffix('f') for v in args.split(',') if v.strip()]
   values=['1' if v=='true' else '0' if v=='false' else v for v in values]
   # Compose arc: rx,ry,rotation,largeArc,sweep,x,y maps directly to SVG.
   parts.append(commands[cmd]+(' '.join(values)))
  if not parts:raise ValueError('No path commands found: '+name)
  paths.append(' '.join(parts))
 if not paths:raise ValueError('No vector paths found: '+name)
 result[key]=paths
out=Path(__file__).resolve().parents[1]/'icons.js'
out.write_text('// GPL-3.0: mechanically ported from upstream SimpIcons ImageVectors.\nexport const paths = '+json.dumps(result,indent=2)+';\nexport function icon(name){return `<svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" fill="currentColor">${(paths[name]||paths.music).map(d=>`<path d="${d}"/>`).join(\'\')}</svg>`;}\n')
print('Ported',len(result),'original icons to',out)
