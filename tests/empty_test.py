import pytest
import json

@pytest.mark.usefixtures("app")
class TestEmptyResources:
    def test_empty_post(self):
        # all the resources should return 404
        res = self.app.get('/posts')
        assert res.status_code == 404
        assert 'not any Post exist' in json.loads(res.data.decode('utf-8'))['message']
        res = self.app.get('/posts/1')
        assert res.status_code == 404
        assert "Post id 1 doesn't exist" in json.loads(res.data.decode('utf-8'))['message']

    def test_empty_persion(self):
        # all the resources should return 404
        res = self.app.get('/persions')
        assert res.status_code == 404
        assert 'not any Persion exist' in json.loads(res.data.decode('utf-8'))['message']
        res = self.app.get('/persions/1')
        assert res.status_code == 404
        assert "Persion id 1 doesn't exist" in json.loads(res.data.decode('utf-8'))['message']

    def test_empty_tag(self):
        # all the resources should return 404
        res = self.app.get('/tags')
        assert res.status_code == 404
        assert 'not any Tag exist' in json.loads(res.data.decode('utf-8'))['message']
        res = self.app.get('/tags/1')
        assert res.status_code == 404
        assert "Tag id 1 doesn't exist" in json.loads(res.data.decode('utf-8'))['message']