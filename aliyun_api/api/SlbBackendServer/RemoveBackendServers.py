# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:27:31 2018

@author: Abner.F
"""


from aliyun_api.common.Slb import UrlRequest

if __name__ == '__main__':

    # SetBackendServers
    '''
    设置后端服务器权重。
    接口说明地址        https://help.aliyun.com/document_detail/27634.html
    
    #"[{'ServerId':'i-wz9fzprkt1ullkni4w38', 'Weight':'50'}]"

    return 返回参数
    参数              类型           描述
    RequestId        String        请求ID。
    LoadBalancerId   String        负载均衡实例ID。
    BackendServers   List         后端服务器列表。
    '''
    
    
    BackendServers = '["i-wz9fzprkt1ullkni4w38"]'

    apiParameter = {
        'Action': 'RemoveBackendServers',
        'RegionId': 'cn-shenzhen',
        'LoadBalancerId': 'lb-wz96sii3zaplkdv9t7n6m',
        'BackendServers': BackendServers
    }

    result = UrlRequest(apiParameter).getResult()
    print(result)

