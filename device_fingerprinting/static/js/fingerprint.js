function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function getMacAddress() {
    try {
        const pc = new RTCPeerConnection();
        pc.createDataChannel("");
        const offer = await pc.createOffer();
        await pc.setLocalDescription(offer);
        
        return new Promise((resolve) => {
            pc.onicecandidate = (ice) => {
                if (ice.candidate) {
                    const parts = ice.candidate.candidate.split(' ');
                    const mac = parts.find(part => /^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$/.test(part));
                    if (mac) {
                        resolve(mac);
                    }
                }
            };
            setTimeout(() => resolve(null), 1000);
        }).finally(() => pc.close());
    } catch (e) {
        console.log('MAC address collection failed:', e);
        return null;
    }
}

async function collectAndSendFingerprint() {
    try {
        console.log('Starting fingerprint collection...');
        const macAddress = await getMacAddress();
        const components = await Fingerprint2.getPromise();
        const values = components.map(component => component.value);
        const fingerprint = Fingerprint2.x64hash128(values.join(''), 31);

        console.log('Fingerprint generated:', fingerprint);

        const fingerprintData = {
            fingerprint: fingerprint,
            userAgent: navigator.userAgent,
            language: navigator.language,
            platform: navigator.platform,
            screenResolution: `${window.screen.width}x${window.screen.height}`,
            timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
            plugins: Array.from(navigator.plugins).map(p => p.name).join(','),
            hardwareConcurrency: navigator.hardwareConcurrency,
            deviceMemory: navigator.deviceMemory,
            colorDepth: window.screen.colorDepth,
            pixelRatio: window.devicePixelRatio,
            touchSupport: 'ontouchstart' in window,
            macAddress: macAddress,
            canvasHash: components.find(c => c.key === 'canvas')?.value || '',
            webglVendor: components.find(c => c.key === 'webgl')?.value?.vendor || '',
            webglRenderer: components.find(c => c.key === 'webgl')?.value?.renderer || '',
            audioHash: components.find(c => c.key === 'audio')?.value || '',
            connectionType: navigator.connection ? navigator.connection.type : '',
            connectionSpeed: navigator.connection ? navigator.connection.effectiveType : '',
            doNotTrack: navigator.doNotTrack === '1' || window.doNotTrack === '1'
        };

        console.log('Sending fingerprint data:', fingerprintData);

        const csrfToken = getCookie('csrftoken');
        console.log('CSRF Token:', csrfToken);

        const response = await fetch('/save-fingerprint/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(fingerprintData)
        });

        console.log('Response status:', response.status);
        const result = await response.json();
        console.log('Response data:', result);

        const resultDiv = document.getElementById('fingerprint-result');
        if (response.ok) {
            resultDiv.innerHTML = `
                <div class="bg-white shadow-lg rounded-lg p-6">
                    <div class="flex items-center justify-between mb-4">
                        <h2 class="text-xl font-bold">Device Fingerprint</h2>
                        <span class="px-3 py-1 rounded ${result.is_new ? 'bg-green-100 text-green-800' : 'bg-blue-100 text-blue-800'}">
                            ${result.is_new ? 'New Device' : 'Known Device'}
                        </span>
                    </div>
                    <div class="grid grid-cols-2 gap-4 text-sm">
                        <div class="col-span-2">
                            <span class="font-semibold">Fingerprint ID:</span>
                            <span class="ml-2 font-mono break-all">${fingerprint}</span>
                        </div>
                        <div><span class="font-semibold">IP Address:</span></div>
                        <div>${result.ip_address}</div>
                        <div><span class="font-semibold">MAC Address:</span></div>
                        <div>${macAddress || 'Not available'}</div>
                        <div><span class="font-semibold">CPU Cores:</span></div>
                        <div>${fingerprintData.hardwareConcurrency || 'Unknown'}</div>
                        <div><span class="font-semibold">Memory:</span></div>
                        <div>${fingerprintData.deviceMemory ? fingerprintData.deviceMemory + 'GB' : 'Unknown'}</div>
                        <div><span class="font-semibold">Screen Resolution:</span></div>
                        <div>${fingerprintData.screenResolution}</div>
                        <div><span class="font-semibold">Color Depth:</span></div>
                        <div>${fingerprintData.colorDepth}-bit</div>
                        <div><span class="font-semibold">Platform:</span></div>
                        <div>${fingerprintData.platform}</div>
                        <div><span class="font-semibold">Browser:</span></div>
                        <div class="break-all">${fingerprintData.userAgent}</div>
                        <div><span class="font-semibold">WebGL Renderer:</span></div>
                        <div class="break-all">${fingerprintData.webglRenderer || 'Not available'}</div>
                        <div><span class="font-semibold">Timezone:</span></div>
                        <div>${fingerprintData.timezone}</div>
                        <div><span class="font-semibold">Language:</span></div>
                        <div>${fingerprintData.language}</div>
                    </div>
                    <div class="mt-4 text-sm text-gray-600">${result.message}</div>
                </div>
            `;
        } else {
            resultDiv.innerHTML = `
                <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-4">
                    <h3 class="font-bold">Error</h3>
                    <p>${result.message || 'Failed to process fingerprint'}</p>
                </div>
            `;
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('fingerprint-result').innerHTML = `
            <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-4">
                <h3 class="font-bold">Error collecting fingerprint</h3>
                <p>${error.message}</p>
            </div>
        `;
    }
}

// Wait for the page to load before collecting fingerprint
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, starting fingerprint collection...');
    setTimeout(collectAndSendFingerprint, 1000);
});
