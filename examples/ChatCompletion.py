# THIS IS OPENAI RESPONSE ON TOOL USE

ChatCompletion(
    id='chatcmpl-9v4HCOiqdbIAhmqvhVSO2UswTouub', 
    choices=[
        Choice(
            finish_reason='tool_calls', 
            index=0, 
            logprobs=None, 
            message=ChatCompletionMessage(
                content=None, 
                refusal=None, 
                role='assistant', 
                function_call=None, 
                tool_calls=[
                    ChatCompletionMessageToolCall(
                        id='call_CXoNv10YpMlIenh89dLJOatu', 
                        function=Function(
                            arguments='{"search_term":"2024 Masters Tournament"}', 
                            name='get_article'), 
                            type='function')
                ]
            )
        )
    ], 
    created=1723388162, 
    model='gpt-4o-mini-2024-07-18', 
    object='chat.completion', 
    service_tier=None, 
    system_fingerprint='fp_48196bc67a', 
    usage=CompletionUsage(
        completion_tokens=18, 
        prompt_tokens=79, 
        total_tokens=97
        )
)

ChatCompletionMessageToolCall(
    id='call_35OWsN8NC2CmmI6wCYWucWgk', 
    function=Function(
        arguments='{"search_term":"2024 Masters Tournament"}', 
        name='get_article'), 
    type='function'
)