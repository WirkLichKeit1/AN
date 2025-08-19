async function encodeAN() {
    const text = document.getElementById('text-input').value.trim();
    const encodeANResult = document.getElementById('encode-AN-result');

    if (!text) {
        encodeANResult.textContent = '[AVISO]: Insira um texto para codificar em AN.';
        encodeANResult.className = 'message warning';
        return;
    }

    try {
        const response = await fetch('/api/translateToAN', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });
        const data = await response.json();
        encodeANResult.textContent = data.result;

        if (data.result.startsWith('[ERRO]:')) {
            encodeANResult.className = 'message error';
        } else {
            encodeANResult.className = 'message success';
        }
    } catch (error) {
        encodeANResult.textContent = '[ERRO]: Falha na comunicação com o servidor.';
        encodeANResult.className = 'message error';
    }
}

async function decodeAN() {
    const AN = document.getElementById('AN-input').value.trim();
    const decodeANResult = document.getElementById('decode-AN-result');

    if (!AN) {
        decodeANResult.textContent = '[AVISO]: Insira um código Alfabeto N para decodificar.';
        decodeANResult.className = 'message warning';
        return;
    }

    try {
        const response = await fetch('/api/translateFromAN', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ AN })
        });
        const data = await response.json();
        decodeANResult.textContent = data.result;

        if (data.result.startsWith('[ERRO]:')) {
            decodeANResult.className = 'message error';
        } else {
            decodeANResult.className = 'message success';
        }
    } catch (error) {
        decodeANResult.textContent = '[ERRO]: Falha na comunicação com o servidor.';
        decodeANResult.className = 'message error';
    }
}

function copyText(elementId) {
    const element = document.getElementById(elementId);
    const text = element.textContent;

    if (!text || text.startsWith('[AVISO]:') || text.startsWith('[ERRO]:') || text.startsWith('[SUCESSO]:')) {
        element.textContent = '[AVISO]: Nada para copiar.';
        element.className = 'message warning';
        setTimeout(() => {
            element.textContent = '';
            element.className = 'message';
        }, 2000);
        return;
    }

    navigator.clipboard.writeText(text).then(() => {
        const originalText = element.textContent;
        element.textContent = '[SUCESSO]: Copiado!';
        element.className = 'message success';
        setTimeout(() => {
            element.textContent = originalText;
            element.className = 'message success';
        }, 2000);
    }).catch(() => {
        element.textContent = '[ERRO]: Falha ao copiar.';
        element.className = 'message error';
        setTimeout(() => {
            element.textContent = '';
            element.className = 'message';
        }, 2000);
    });
}
