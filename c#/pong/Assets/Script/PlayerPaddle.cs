using UnityEngine;

public class PlayerPaddle : Paddle
{
    public Vector2 direction { get; private set; }

    private void Update()
    {
        if (Input.GetKey(KeyCode.W) || Input.GetKey(KeyCode.UpArrow))
        {
            //this.direction = Vector2.up;
            this.movePaddleTop();
        }
        else if (Input.GetKey(KeyCode.S) || Input.GetKey(KeyCode.DownArrow))
        {
            //this.direction = Vector2.down;
            this.movePaddleBottom();
        }
        else
        {
            //this.direction = Vector2.zero;
            this.movePaddleMiddle();
        }
    }

    public void movePaddleTop()
    {
        this.rigidbody.position = new Vector2(this.rigidbody.position.x, 3.4f);
    }

    public void movePaddleMiddle()
    {
        this.rigidbody.position = new Vector2(this.rigidbody.position.x, 0f);
    }

    public void movePaddleBottom()
    {
        this.rigidbody.position = new Vector2(this.rigidbody.position.x, -3.4f);
    }

    private void FixedUpdate()
    {
        if (this.direction.sqrMagnitude != 0)
        {
            this.rigidbody.AddForce(this.direction * this.speed);
        }
    }

}