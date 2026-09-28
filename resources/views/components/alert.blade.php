    @if ($type === 'error')
        <div style="padding: 10px; border: 1px solid red; margin: 10px 0;">
    @else
        <div style="padding: 10px; border: 1px solid green; margin: 10px 0;">
    @endif
            <strong>{{ ucfirst($type) }}</strong> {{ $message }}
        </div>