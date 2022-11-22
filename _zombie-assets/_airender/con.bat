.\_zombie-assets\_airender\aihack.exe .\_zombie-assets\_airender\aihack.dll ISZ-Win64-Shipping.exe
echo aioverride = cpu.hook(zombie.mesh, zombie.bp, ai.bptree).render(ai) > AI-Hook0.bin
echo with work(aioverride, 'wb','rb+') as scan: > AI-Hook1.bin
echo console.inject(ticks(20)).ISZ-Win64-Shipping.exe > AI-Hook2.bin
echo start .\hooks\hook.exe > StartApp.bin