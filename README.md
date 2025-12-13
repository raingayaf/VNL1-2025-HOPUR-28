MIT License
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# MIKILVÆGT, ef þú vilt fá nýtt mót:
Til þess að gera nýtt mót í kerfi okkar farðu neðst í skjalið.


# hvernig er forritið ræst?:
Þar sem við erum ekki með neina import pakka þar sem nýjir notendur þurfa að installa er hægt að nota hefbunda leið í cmd(command line) til að keyra forritið. Hér fyrir neðan er nokkur skref sem hjálpa við uppkeyrslu á forritinu okkar:

cmd = command line
cd = change directory

1. opna cmd, hægt að gera það með því að fara í "search bar" í windows og skrifa inn cmd eða command line.
2. Þegar kveikt er á cmd er gott að athuga hvort þú sért ekki örugglega með python útgáfu nýrri en 3.8 þá ertu öruggur. Sláðu inn "python --version" eða "py --version".
3. Notaðu cd til að færa þig að möppunni þar sem forritið er geymt. t.d. "cd C:/Users/karla/Documents/GitHub/VNL1-2025-HOPUR-28" var mín leið til að komast að forritinu sem er geymt hjá mér.
4. Sláðu inn "py main.py" eða "python main.py" og byrjar þú þá á heimaskjá forritsins.


# youtube linkur:
https://www.youtube.com/watch?v=BEI9qRqiKVM


# Upplýsingar um CSV möppur:
matches.csv: hefur upplýsingar um mót sem er núþegar búið og þegar keyrt er forritið er hægt að sjá dagskrá í gegnum mótshaldara.
players.csv inniheldur upplýsingar um alla leikmenn í kerfi og eru þeir skráðir með tengingu við liðið sitt og leikmanna auðkenni o.fl.
teams.csv: inniheldur öll lið í kerfi sem eru skráð með nokkrum upplýsingum svosem team_name, team_id og captain_handle o.fl.
tournaments.csv: inniheldur mót sem eru skráð í kerfi og eru þau skráð með nokkrum upplýsngum eins og tournament_id, name, venue o.fl.

# MIKILVÆGT, ef þú vilt fá nýtt mót:
Til þess að gera nýtt mót í kerfi okkar þarf að skrá mót og gera síðan 16 lið svo hægt sé að keyra mót í gegnum mótshaldara.
Hér höfum við lista af nýjum 16 liðum sem hægt er að copy-paste inní teams.csv svo ekki verða 16 lið heldur 32.

17,Quantum Queue Quarrel,QuantumQuinn,https://example.com/quantum_queue_quarrel,ASCII_QUBIT_QUEUE
18,Deadlock Dragons,DeadlockDagur,https://example.com/deadlock_dragons,ASCII_DRAGON_LOCK
19,Bitshift Bandits,BitshiftBaldur,https://example.com/bitshift_bandits,ASCII_SHIFT_ARROWS
20,ForkBomb Fighters,ForkBombFreyr,https://example.com/forkbomb_fighters,ASCII_FORK_BOMB
21,Kernel Panic Knights,KernelPanicKatrin,https://example.com/kernel_panic_knights,ASCII_PANIC_SHIELD
22,BlueScreen Buccaneers,BlueScreenBjartey,https://example.com/bluescreen_buccaneers,ASCII_BSOD_FLAG
23,Heisenbug Hunters,HeisenbugHelgi,https://example.com/heisenbug_hunters,ASCII_GHOST_BUG
24,NullByte Nomads,NullByteNökkvi,https://example.com/nullbyte_nomads,ASCII_ZERO_BYTE
25,Runtime Raiders,RuntimeRuna,https://example.com/runtime_raiders,ASCII_STOPWATCH_SWORD
26,Semaphore Sentinels,SemaphoreSólveig,https://example.com/semaphore_sentinels,ASCII_SIGNAL_TOWER
27,Garbage Collector Guild,GarbageGunnar,https://example.com/garbage_collector_guild,ASCII_TRASH_EMBLEM
28,Patch Notes Pirates,PatchNotesPétur,https://example.com/patch_notes_pirates,ASCII_PATCH_SKULL
29,Buffer Overrun Brigade,BufferOverrunBerglind,https://example.com/buffer_overrun_brigade,ASCII_BUFFER_BREACH
30,Latency Legends,LatencyLoki,https://example.com/latency_legends,ASCII_PING_CROWN
31,Packet Loss Phantoms,PacketLossPatrekur,https://example.com/packet_loss_phantoms,ASCII_BROKEN_PACKET
32,Exception Executioners,ExceptionEydis,https://example.com/exception_executioners,ASCII_THROWN_AXE

Til þess að spara ykkur hausverkin að stimpla inn 16-lið í gegnum fyrirliða, einfaldlega copy-paste þennan lista í teams.csv.
Með teams þarf auðvitað að fylgja með leikmenn og fylgir hér listi sem tengjast þessum liðum.

P049,Quinn Qubit,2003-02-11,Quantumgata 1 Reykjavik,+3546110049,quinn.qubit@example.com,https://twitch.tv/QuantumQuinn,QuantumQuinn,Quantum Queue Quarrel
P050,Helga Hadamard,2004-06-18,Quantumgata 2 Reykjavik,+3546110050,helga.hadamard@example.com,https://github.com/HadamardHelga,HadamardHelga,Quantum Queue Quarrel
P051,Einar Entangle,2005-09-04,Quantumgata 3 Reykjavik,+3546110051,einar.entangle@example.com,https://twitter.com/EntangleEinar,EntangleEinar,Quantum Queue Quarrel
P052,Dagur Deadlock,2003-01-27,Lockgata 1 Reykjavik,+3546110052,dagur.deadlock@example.com,https://twitch.tv/DeadlockDagur,DeadlockDagur,Deadlock Dragons
P053,Freydis Fork,2004-04-09,Lockgata 2 Reykjavik,+3546110053,freydis.fork@example.com,https://github.com/ForkSafeFreydis,ForkSafeFreydis,Deadlock Dragons
P054,Orri Order,2005-11-16,Lockgata 3 Reykjavik,+3546110054,orri.order@example.com,https://twitter.com/LockOrderOrri,LockOrderOrri,Deadlock Dragons
P055,Baldur Bitshift,2003-03-14,Bitgata 1 Reykjavik,+3546110055,baldur.bitshift@example.com,https://twitch.tv/BitshiftBaldur,BitshiftBaldur,Bitshift Bandits
P056,Sunna SignBit,2004-08-21,Bitgata 2 Reykjavik,+3546110056,sunna.signbit@example.com,https://github.com/SignBitSunna,SignBitSunna,Bitshift Bandits
P057,Aron Arithmetic,2005-12-02,Bitgata 3 Reykjavik,+3546110057,aron.arithmetic@example.com,https://twitter.com/ShiftAndMaskAron,ShiftAndMaskAron,Bitshift Bandits
P058,Freyr Forkbomb,2003-07-07,Forkgata 1 Reykjavik,+3546110058,freyr.forkbomb@example.com,https://twitch.tv/ForkBombFreyr,ForkBombFreyr,ForkBomb Fighters
P059,Lilja Loopstorm,2004-02-26,Forkgata 2 Reykjavik,+3546110059,lilja.loopstorm@example.com,https://github.com/LoopStormLilja,LoopStormLilja,ForkBomb Fighters
P060,Hrafn Heapspawn,2005-10-19,Forkgata 3 Reykjavik,+3546110060,hrafn.heapspawn@example.com,https://twitter.com/HeapSpawnHrafn,HeapSpawnHrafn,ForkBomb Fighters
P061,Katrin Kernel,2003-05-12,Kernelgata 1 Reykjavik,+3546110061,katrin.kernel@example.com,https://twitch.tv/KernelPanicKatrin,KernelPanicKatrin,Kernel Panic Knights
P062,Stefan Stacktrace,2004-09-03,Kernelgata 2 Reykjavik,+3546110062,stefan.stacktrace@example.com,https://github.com/StacktraceStefan,StacktraceStefan,Kernel Panic Knights
P063,Una Uptime,2005-01-30,Kernelgata 3 Reykjavik,+3546110063,una.uptime@example.com,https://twitter.com/UptimeUna,UptimeUna,Kernel Panic Knights
P064,Bjartey Bluescreen,2003-06-06,Crashgata 1 Reykjavik,+3546110064,bjartey.bluescreen@example.com,https://twitch.tv/BlueScreenBjartey,BlueScreenBjartey,BlueScreen Buccaneers
P065,Andri Dumpfile,2004-11-11,Crashgata 2 Reykjavik,+3546110065,andri.dumpfile@example.com,https://github.com/DumpfileAndri,DumpfileAndri,BlueScreen Buccaneers
P066,Runa Reboot,2005-04-22,Crashgata 3 Reykjavik,+3546110066,runa.reboot@example.com,https://twitter.com/RebootRuna,RebootRuna,BlueScreen Buccaneers
P067,Helgi Heisenbug,2003-08-08,Buggata 1 Reykjavik,+3546110067,helgi.heisenbug@example.com,https://twitch.tv/HeisenbugHelgi,HeisenbugHelgi,Heisenbug Hunters
P068,Sigrid Schrödinger,2004-12-15,Buggata 2 Reykjavik,+3546110068,sigrid.schrodinger@example.com,https://github.com/QuantumCatSigrid,QuantumCatSigrid,Heisenbug Hunters
P069,Kristjan KernelRace,2005-02-05,Buggata 3 Reykjavik,+3546110069,kristjan.kernelrace@example.com,https://twitter.com/RaceBugKristjan,RaceBugKristjan,Heisenbug Hunters
P070,Nökkvi Nullbyte,2003-03-03,Bytegata 1 Reykjavik,+3546110070,nokkvi.nullbyte@example.com,https://twitch.tv/NullByteNokkvi,NullByteNokkvi,NullByte Nomads
P071,Elin EmptyPtr,2004-07-17,Bytegata 2 Reykjavik,+3546110071,elin.emptyptr@example.com,https://github.com/EmptyPtrElin,EmptyPtrElin,NullByte Nomads
P072,Markus MemoryGap,2005-11-28,Bytegata 3 Reykjavik,+3546110072,markus.memorygap@example.com,https://twitter.com/MemoryGapMarkus,MemoryGapMarkus,NullByte Nomads
P073,Runa Runtime,2003-01-09,Runtimegata 1 Reykjavik,+3546110073,runa.runtime@example.com,https://twitch.tv/RuntimeRuna,RuntimeRuna,Runtime Raiders
P074,Jon JITter,2004-06-14,Runtimegata 2 Reykjavik,+3546110074,jon.jitter@example.com,https://github.com/JITJon,JITJon,Runtime Raiders
P075,Helena Hotpath,2005-09-30,Runtimegata 3 Reykjavik,+3546110075,helena.hotpath@example.com,https://twitter.com/HotPathHelena,HotPathHelena,Runtime Raiders
P076,Sólveig Semaphore,2003-04-04,Syncgata 1 Reykjavik,+3546110076,solveig.semaphore@example.com,https://twitch.tv/SemaphoreSolveig,SemaphoreSolveig,Semaphore Sentinels
P077,Arni Atomic,2004-10-10,Syncgata 2 Reykjavik,+3546110077,arni.atomic@example.com,https://github.com/AtomicArni,AtomicArni,Semaphore Sentinels
P078,Edda Eventlock,2005-12-19,Syncgata 3 Reykjavik,+3546110078,edda.eventlock@example.com,https://twitter.com/EventLockEdda,EventLockEdda,Semaphore Sentinels
P079,Gunnar Garbage,2003-05-25,Heapgata 1 Reykjavik,+3546110079,gunner.garbage@example.com,https://twitch.tv/GarbageGunnar,GarbageGunnar,Garbage Collector Guild
P080,Tomas Tracer,2004-08-08,Heapgata 2 Reykjavik,+3546110080,tomas.tracer@example.com,https://github.com/HeapTracerTomas,HeapTracerTomas,Garbage Collector Guild
P081,Silja Sweep,2005-03-16,Heapgata 3 Reykjavik,+3546110081,silja.sweep@example.com,https://twitter.com/SweepPhaseSilja,SweepPhaseSilja,Garbage Collector Guild
P082,Pétur Patchnotes,2003-02-02,Pirategata 1 Reykjavik,+3546110082,petur.patch@example.com,https://twitch.tv/PatchNotesPetur,PatchNotesPetur,Patch Notes Pirates
P083,Arna Update,2004-07-27,Pirategata 2 Reykjavik,+3546110083,arna.update@example.com,https://github.com/UpdateArna,UpdateArna,Patch Notes Pirates
P084,Bjorn Backport,2005-11-05,Pirategata 3 Reykjavik,+3546110084,bjorn.backport@example.com,https://twitter.com/BackportBjorn,BackportBjorn,Patch Notes Pirates
P085,Berglind Buffer,2003-06-01,Bufferbraut 1 Reykjavik,+3546110085,berglind.buffer@example.com,https://twitch.tv/BufferOverrunBerglind,BufferOverrunBerglind,Buffer Overrun Brigade
P086,Olaf Offset,2004-09-19,Bufferbraut 2 Reykjavik,+3546110086,olaf.offset@example.com,https://github.com/OffsetOlaf,OffsetOlaf,Buffer Overrun Brigade
P087,Klara Canary,2005-01-23,Bufferbraut 3 Reykjavik,+3546110087,klara.canary@example.com,https://twitter.com/StackCanaryKlara,StackCanaryKlara,Buffer Overrun Brigade
P088,Loki Latency,2003-08-14,Pinggata 1 Reykjavik,+3546110088,loki.latency@example.com,https://twitch.tv/LatencyLoki,LatencyLoki,Latency Legends
P089,Ina Interrupt,2004-03-09,Pinggata 2 Reykjavik,+3546110089,ina.interrupt@example.com,https://github.com/InterruptIna,InterruptIna,Latency Legends
P090,Ragnar Roundtrip,2005-12-01,Pinggata 3 Reykjavik,+3546110090,ragnar.roundtrip@example.com,https://twitter.com/RoundTripRagnar,RoundTripRagnar,Latency Legends
P091,Patrekur Packetloss,2003-04-18,Netgata 1 Reykjavik,+3546110091,patrekur.packetloss@example.com,https://twitch.tv/PacketLossPatrekur,PacketLossPatrekur,Packet Loss Phantoms
P092,Helena Handshake,2004-07-07,Netgata 2 Reykjavik,+3546110092,helena.handshake@example.com,https://github.com/HandshakeHelena,HandshakeHelena,Packet Loss Phantoms
P093,Steinar Streamdrop,2005-10-26,Netgata 3 Reykjavik,+3546110093,steinar.streamdrop@example.com,https://twitter.com/StreamDropSteinar,StreamDropSteinar,Packet Loss Phantoms
P094,Eydis Exception,2003-01-15,Throwgata 1 Reykjavik,+3546110094,eydis.exception@example.com,https://twitch.tv/ExceptionEydis,ExceptionEydis,Exception Executioners
P095,Aron Abort,2004-05-29,Throwgata 2 Reykjavik,+3546110095,aron.abort@example.com,https://github.com/AbortAron,AbortAron,Exception Executioners
P096,Vera Vtable,2005-09-12,Throwgata 3 Reykjavik,+3546110096,vera.vtable@example.com,https://twitter.com/VtableVera,VtableVera,Exception Executioners

Til að auðvelda ykkur hausverkin að þurfa ekki að stimpla inn 48 nýja leikmenn í kerfið getið þið copy-pase þennan lista inní players.csv