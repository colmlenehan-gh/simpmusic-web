import {test} from 'node:test';
import assert from 'node:assert/strict';
import {videoID,parseLRC,escapeHTML,validateBackup,safeImage,formatTime} from '../core.js';
test('YouTube URLs accept known hosts and reject lookalikes and invalid IDs',()=>{assert.equal(videoID('https://youtu.be/MSRcC626prw?t=5'),'MSRcC626prw');assert.equal(videoID('https://music.youtube.com/watch?v=MSRcC626prw'),'MSRcC626prw');assert.equal(videoID('https://youtube.com.evil.test/watch?v=MSRcC626prw'),null);assert.equal(videoID('javascript:alert(1)'),null);assert.equal(videoID('bad'),null);});
test('LRC supports repeated timestamps and chronological order',()=>{assert.deepEqual(parseLRC('[ar:Artist]\n[01:02.50][00:02.00]hello\n[00:01]first'),[{time:1,text:'first'},{time:2,text:'hello'},{time:62.5,text:'hello'}]);});
test('Untrusted metadata cannot become markup',()=>{assert.equal(escapeHTML('<img onerror="x">'), '&lt;img onerror=&quot;x&quot;&gt;');assert.equal(safeImage('javascript:alert(1)'), '');assert.equal(safeImage('https://evil.test/x.png'), '');});
test('Malformed or foreign backups are rejected before merging',()=>{assert.throws(()=>validateBackup({version:1,tracks:[{id:'x',kind:'youtube',videoId:'bad',title:'x',artist:'x'}],likes:[],playlists:[]}));assert.throws(()=>validateBackup({version:2}));assert.equal(validateBackup({version:1,tracks:[],likes:[],playlists:[]}).version,1);});
test('Invalid duration never produces NaN in UI',()=>{assert.equal(formatTime(NaN),'0:00');assert.equal(formatTime(Infinity),'0:00');assert.equal(formatTime(125.4),'2:05');});
