import Connection from '../../helpers/Connection.js'
import BaseUrl from '../../helpers/BaseUrl.js'

export async function post (context, data) {
  const url = BaseUrl.getUrl('add')
  const request = await Connection.request('post', url, data)
  return request
}

export async function get (context) {
  const url = BaseUrl.getUrl('get')
  const request = await Connection.request('get', url)
  context.commit('setProperty', { key: 'questions', data: request.data })
  return request
}
